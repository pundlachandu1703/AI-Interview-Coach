// =========================================================
// AI INTERVIEW COACH - FINAL JAVASCRIPT
// =========================================================


// =========================================================
// GLOBAL VARIABLES
// =========================================================

let selectedRole = "";

let totalQuestions = 5;

let currentQuestionIndex = 0;

let currentQuestion = "";

let usedQuestions = [];

let scores = [];


// =========================================================
// GET ELEMENTS
// =========================================================

const startScreen =
    document.getElementById("startScreen");

const interviewScreen =
    document.getElementById("interviewScreen");

const resultScreen =
    document.getElementById("resultScreen");

const startBtn =
    document.getElementById("startBtn");

const submitBtn =
    document.getElementById("submitBtn");

const nextBtn =
    document.getElementById("nextBtn");

const finishBtn =
    document.getElementById("finishBtn");

const restartBtn =
    document.getElementById("restartBtn");

const roleSelect =
    document.getElementById("role");

const questionCountSelect =
    document.getElementById("questionCount");

const answerBox =
    document.getElementById("answer");

const questionText =
    document.getElementById("questionText");

const loading =
    document.getElementById("loading");

const feedback =
    document.getElementById("feedback");


// =========================================================
// START INTERVIEW
// =========================================================

startBtn.addEventListener(
    "click",
    startInterview
);


async function startInterview() {

    const role =
        roleSelect.value;


    const count =
        parseInt(
            questionCountSelect.value
        );


    // -----------------------------------------
    // VALIDATION
    // -----------------------------------------

    if (!role) {

        document.getElementById(
            "startError"
        ).textContent =
            "Please select a job role.";

        return;
    }


    // -----------------------------------------
    // RESET INTERVIEW
    // -----------------------------------------

    selectedRole = role;

    totalQuestions = count;

    currentQuestionIndex = 0;

    usedQuestions = [];

    scores = [];


    // -----------------------------------------
    // UPDATE UI
    // -----------------------------------------

    document.getElementById(
        "roleDisplay"
    ).textContent =
        selectedRole;

    document.getElementById(
        "totalQuestions"
    ).textContent =
        totalQuestions;


    startScreen.classList.add(
        "hidden"
    );

    interviewScreen.classList.remove(
        "hidden"
    );


    // -----------------------------------------
    // LOAD FIRST QUESTION
    // -----------------------------------------

    await loadQuestion();

}


// =========================================================
// LOAD QUESTION
// =========================================================

async function loadQuestion() {

    showLoading();


    try {

        const response =
            await fetch(
                "/question",
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        role:
                            selectedRole,

                        used_questions:
                            usedQuestions

                    })

                }
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.error ||
                "Unable to load question."
            );

        }


        // -------------------------------------
        // STORE QUESTION
        // -------------------------------------

        currentQuestion =
            data.question;


        usedQuestions.push(
            currentQuestion
        );


        // -------------------------------------
        // UPDATE QUESTION
        // -------------------------------------

        questionText.textContent =
            currentQuestion;


        document.getElementById(
            "questionNumber"
        ).textContent =
            currentQuestionIndex + 1;


        document.getElementById(
            "currentQuestion"
        ).textContent =
            currentQuestionIndex + 1;


        // -------------------------------------
        // UPDATE PROGRESS
        // -------------------------------------

        const progress =
            (
                currentQuestionIndex
                /
                totalQuestions
            ) * 100;


        document.getElementById(
            "progressFill"
        ).style.width =
            Math.max(
                progress,
                5
            ) + "%";


        // -------------------------------------
        // CLEAR ANSWER
        // -------------------------------------

        answerBox.value = "";

        updateWordCount();


        // -------------------------------------
        // HIDE OLD FEEDBACK
        // -------------------------------------

        feedback.classList.add(
            "hidden"
        );


        submitBtn.disabled = false;


        submitBtn.textContent =
            "🧠 Evaluate My Answer";


        document.getElementById(
            "answerError"
        ).textContent = "";


        // -------------------------------------
        // SCROLL
        // -------------------------------------

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });


    }

    catch (error) {

        console.error(
            "Question error:",
            error
        );


        document.getElementById(
            "answerError"
        ).textContent =
            error.message;


    }

    finally {

        hideLoading();

    }

}


// =========================================================
// SUBMIT ANSWER
// =========================================================

submitBtn.addEventListener(
    "click",
    evaluateCurrentAnswer
);


async function evaluateCurrentAnswer() {

    const answer =
        answerBox.value.trim();


    // -----------------------------------------
    // VALIDATION
    // -----------------------------------------

    if (!answer) {

        document.getElementById(
            "answerError"
        ).textContent =
            "Please enter your answer before submitting.";

        answerBox.focus();

        return;
    }


    if (answer.split(/\s+/).length < 3) {

        document.getElementById(
            "answerError"
        ).textContent =
            "Please provide a more detailed answer.";

        answerBox.focus();

        return;
    }


    document.getElementById(
        "answerError"
    ).textContent = "";


    showLoading();


    submitBtn.disabled = true;


    try {

        const response =
            await fetch(
                "/evaluate",
                {

                    method: "POST",

                    headers: {

                        "Content-Type":
                            "application/json"

                    },

                    body: JSON.stringify({

                        role:
                            selectedRole,

                        question:
                            currentQuestion,

                        answer:
                            answer

                    })

                }
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.error ||
                "Evaluation failed."
            );

        }


        // -------------------------------------
        // SAVE SCORE
        // -------------------------------------

        scores.push(
            Number(data.score)
        );


        // -------------------------------------
        // DISPLAY FEEDBACK
        // -------------------------------------

        displayFeedback(data);


    }

    catch (error) {

        console.error(
            "Evaluation error:",
            error
        );


        document.getElementById(
            "answerError"
        ).textContent =
            error.message;


        submitBtn.disabled = false;

    }

    finally {

        hideLoading();

    }

}


// =========================================================
// DISPLAY FEEDBACK
// =========================================================

function displayFeedback(data) {

    feedback.classList.remove(
        "hidden"
    );


    // -----------------------------------------
    // SCORE
    // -----------------------------------------

    document.getElementById(
        "score"
    ).textContent =
        Math.round(
            data.score
        );


    // -----------------------------------------
    // FEEDBACK
    // -----------------------------------------

    document.getElementById(
        "feedbackText"
    ).textContent =
        data.feedback;


    // -----------------------------------------
    // SCORE BREAKDOWN
    // -----------------------------------------

    document.getElementById(
        "keywordScore"
    ).textContent =
        Math.round(
            data.keyword_score
        ) + "%";


    document.getElementById(
        "similarityScore"
    ).textContent =
        Math.round(
            data.similarity_score
        ) + "%";


    document.getElementById(
        "lengthScore"
    ).textContent =
        Math.round(
            data.length_score
        ) + "%";


    // -----------------------------------------
    // PERFECT ANSWER
    // -----------------------------------------

    document.getElementById(
        "perfectAnswer"
    ).textContent =
        data.perfect_answer;


    // -----------------------------------------
    // STRENGTHS
    // -----------------------------------------

    createList(
        "strengths",
        data.strengths
    );


    // -----------------------------------------
    // WEAKNESSES
    // -----------------------------------------

    createList(
        "weaknesses",
        data.weaknesses
    );


    // -----------------------------------------
    // MATCHED KEYWORDS
    // -----------------------------------------

    createKeywords(
        "matchedKeywords",
        data.matched_keywords,
        "matched"
    );


    // -----------------------------------------
    // MISSING KEYWORDS
    // -----------------------------------------

    createKeywords(
        "missingKeywords",
        data.missing_keywords,
        "missing"
    );


    // -----------------------------------------
    // CHANGE BUTTON
    // -----------------------------------------

    if (
        currentQuestionIndex >=
        totalQuestions - 1
    ) {

        nextBtn.textContent =
            "🏆 View Final Result";

    }

    else {

        nextBtn.textContent =
            "Next Question →";

    }


    // -----------------------------------------
    // SCROLL TO FEEDBACK
    // -----------------------------------------

    setTimeout(() => {

        feedback.scrollIntoView({

            behavior: "smooth",

            block: "start"

        });

    }, 100);

}


// =========================================================
// CREATE FEEDBACK LIST
// =========================================================

function createList(
    elementId,
    items
) {

    const element =
        document.getElementById(
            elementId
        );


    element.innerHTML = "";


    if (
        !items ||
        items.length === 0
    ) {

        const li =
            document.createElement(
                "li"
            );

        li.textContent =
            "No specific points identified.";

        element.appendChild(
            li
        );

        return;

    }


    items.forEach(
        item => {

            const li =
                document.createElement(
                    "li"
                );

            li.textContent =
                item;

            element.appendChild(
                li
            );

        }
    );

}


// =========================================================
// CREATE KEYWORDS
// =========================================================

function createKeywords(
    elementId,
    keywords,
    type
) {

    const container =
        document.getElementById(
            elementId
        );


    container.innerHTML = "";


    if (
        !keywords ||
        keywords.length === 0
    ) {

        const span =
            document.createElement(
                "span"
            );

        span.className =
            "no-keywords";

        if (type === "matched") {

            span.textContent =
                "No keywords detected.";

        }

        else {

            span.textContent =
                "Great! No major concepts missing.";

        }


        container.appendChild(
            span
        );

        return;

    }


    keywords.forEach(
        keyword => {

            const span =
                document.createElement(
                    "span"
                );


            span.className =
                "keyword " + type;


            span.textContent =
                keyword;


            container.appendChild(
                span
            );

        }
    );

}


// =========================================================
// NEXT QUESTION
// =========================================================

nextBtn.addEventListener(
    "click",
    nextQuestion
);


async function nextQuestion() {

    // -----------------------------------------
    // CHECK IF INTERVIEW IS COMPLETE
    // -----------------------------------------

    if (
        currentQuestionIndex >=
        totalQuestions - 1
    ) {

        showFinalResult();

        return;

    }


    // -----------------------------------------
    // NEXT
    // -----------------------------------------

    currentQuestionIndex++;


    await loadQuestion();

}


// =========================================================
// FINISH INTERVIEW
// =========================================================

finishBtn.addEventListener(
    "click",
    showFinalResult
);


function showFinalResult() {

    if (scores.length === 0) {

        return;

    }


    // -----------------------------------------
    // CALCULATE RESULTS
    // -----------------------------------------

    const total =
        scores.reduce(
            (sum, score) =>
                sum + score,
            0
        );


    const average =
        total /
        scores.length;


    const best =
        Math.max(
            ...scores
        );


    // -----------------------------------------
    // UPDATE RESULT SCREEN
    // -----------------------------------------

    document.getElementById(
        "finalScore"
    ).textContent =
        Math.round(
            average
        );


    document.getElementById(
        "answeredCount"
    ).textContent =
        scores.length;


    document.getElementById(
        "averageScore"
    ).textContent =
        Math.round(
            average
        );


    document.getElementById(
        "bestScore"
    ).textContent =
        Math.round(
            best
        );


    // -----------------------------------------
    // RESULT MESSAGE
    // -----------------------------------------

    let message;


    if (average >= 85) {

        message =
            "🌟 Excellent! You are highly prepared for the interview.";

    }

    else if (average >= 70) {

        message =
            "👏 Very Good! A little more practice will make you stronger.";

    }

    else if (average >= 50) {

        message =
            "👍 Good Start! Focus on the areas identified in your feedback.";

    }

    else {

        message =
            "📚 Keep Practicing! Review the concepts and try another interview.";

    }


    document.getElementById(
        "resultMessage"
    ).textContent =
        message;


    // -----------------------------------------
    // SWITCH SCREEN
    // -----------------------------------------

    interviewScreen.classList.add(
        "hidden"
    );


    resultScreen.classList.remove(
        "hidden"
    );


    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

}


// =========================================================
// RESTART INTERVIEW
// =========================================================

restartBtn.addEventListener(
    "click",
    restartInterview
);


function restartInterview() {

    selectedRole = "";

    totalQuestions = 5;

    currentQuestionIndex = 0;

    currentQuestion = "";

    usedQuestions = [];

    scores = [];


    roleSelect.value = "";


    document.getElementById(
        "questionCount"
    ).value = "5";


    resultScreen.classList.add(
        "hidden"
    );


    interviewScreen.classList.add(
        "hidden"
    );


    startScreen.classList.remove(
        "hidden"
    );


    document.getElementById(
        "startError"
    ).textContent = "";


    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

}


// =========================================================
// WORD COUNT
// =========================================================

answerBox.addEventListener(
    "input",
    updateWordCount
);


function updateWordCount() {

    const text =
        answerBox.value.trim();


    if (!text) {

        document.getElementById(
            "wordCount"
        ).textContent =
            "0";

        return;

    }


    const words =
        text.split(
            /\s+/
        );


    document.getElementById(
        "wordCount"
    ).textContent =
        words.length;

}


// =========================================================
// LOADING
// =========================================================

function showLoading() {

    loading.classList.remove(
        "hidden"
    );

}


function hideLoading() {

    loading.classList.add(
        "hidden"
    );

}


// =========================================================
// ENTER KEY SHORTCUT
// =========================================================

answerBox.addEventListener(
    "keydown",
    function(event) {

        // Ctrl + Enter
        // submits the answer

        if (
            event.ctrlKey &&
            event.key === "Enter"
        ) {

            event.preventDefault();

            evaluateCurrentAnswer();

        }

    }
);


// =========================================================
// INITIAL STATE
// =========================================================

document.addEventListener(
    "DOMContentLoaded",
    function() {

        startScreen.classList.remove(
            "hidden"
        );


        interviewScreen.classList.add(
            "hidden"
        );


        resultScreen.classList.add(
            "hidden"
        );


        feedback.classList.add(
            "hidden"
        );


        hideLoading();

    }
);
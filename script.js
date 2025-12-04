const displayEl = document.getElementById("display");
const historyEl = document.getElementById("history");
const buttons = document.querySelectorAll(".calculator-buttons .btn");

let currentValue = "0";
let historyValue = "";
let justEvaluated = false;

function updateDisplay() {
    displayEl.textContent = currentValue;
    historyEl.textContent = historyValue;
}

function clearAll() {
    currentValue = "0";
    historyValue = "";
    justEvaluated = false;
    updateDisplay();
}

function deleteLast() {
    if (justEvaluated) {
        // after result, DEL should clear everything
        clearAll();
        return;
    }

    if (currentValue.length <= 1) {
        currentValue = "0";
    } else {
        currentValue = currentValue.slice(0, -1);
    }
    updateDisplay();
}

function appendValue(value) {
    if (justEvaluated && /[0-9.]/.test(value)) {
        // start new number after evaluation
        currentValue = value === "." ? "0." : value;
        justEvaluated = false;
    } else if (currentValue === "0" && value !== "." && !isNaN(value)) {
        // replace leading 0 for numbers
        currentValue = value;
    } else {
        // avoid multiple dots in one number chunk
        if (value === ".") {
            const parts = currentValue.split(/[\+\-\*\/%]/);
            const lastPart = parts[parts.length - 1];
            if (lastPart.includes(".")) return;
        }
        currentValue += value;
    }
    updateDisplay();
}

function togglePlusMinus() {
    if (currentValue === "0") return;

    // find last number segment
    const match = currentValue.match(/(-?\d*\.?\d+)(?!.*\d)/);
    if (!match) return;

    const numberStr = match[1];
    const startIndex = match.index;
    const before = currentValue.slice(0, startIndex);
    const after = currentValue.slice(startIndex + numberStr.length);

    const toggled = numberStr.startsWith("-")
        ? numberStr.slice(1)
        : "-" + numberStr;

    currentValue = before + toggled + after;
    updateDisplay();
}

function evaluateExpression() {
    try {
        // Use a safe-ish evaluation:
        // allow only digits, +-*/%. and spaces
        const safeExpr = currentValue.replace(/[^0-9+\-*/%.]/g, "");
        if (!safeExpr) return;

        const result = Function(`"use strict"; return (${safeExpr})`)();

        if (result === undefined || result === null || isNaN(result)) {
            return;
        }

        historyValue = currentValue + " =";
        currentValue = String(result);
        justEvaluated = true;
        updateDisplay();
    } catch (err) {
        currentValue = "Error";
        justEvaluated = true;
        updateDisplay();
    }
}

buttons.forEach((btn) => {
    const value = btn.getAttribute("data-value");
    const action = btn.getAttribute("data-action");

    btn.addEventListener("click", () => {
        if (action === "clear") {
            clearAll();
            return;
        }
        if (action === "delete") {
            deleteLast();
            return;
        }
        if (action === "plusminus") {
            togglePlusMinus();
            return;
        }
        if (action === "equals") {
            evaluateExpression();
            return;
        }
        if (value) {
            appendValue(value);
        }
    });
});

// Optional: keyboard support
document.addEventListener("keydown", (e) => {
    const key = e.key;

    if (/\d/.test(key)) {
        appendValue(key);
    } else if (key === ".") {
        appendValue(".");
    } else if (["+", "-", "*", "/"].includes(key)) {
        appendValue(key);
    } else if (key === "Enter" || key === "=") {
        e.preventDefault();
        evaluateExpression();
    } else if (key === "Backspace") {
        deleteLast();
    } else if (key.toLowerCase() === "c" || key === "Escape") {
        clearAll();
    }
});

// Initialize display on first load
updateDisplay();

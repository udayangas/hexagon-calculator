function calculate(event) {
	let activeElementId = event.target.id;
	let a, d, s, R, r, A, P;

	// Helper function to get input value as a float or null
	const getInputValue = (id) =>
		parseFloat(document.getElementById(id).value) || null;

	// Get current values from all inputs
	a = getInputValue('side');
	d = getInputValue('longDiagonal');
	s = getInputValue('shortDiagonal');
	R = getInputValue('circumcircleRadius');
	r = getInputValue('apothem');
	A = getInputValue('area');
	P = getInputValue('perimeter');

	// Determine 'a' (side length) based on the active input field
	if (activeElementId === 'side' && a !== null) {
		// 'a' is already set if 'side' was the active element
	} else if (activeElementId === 'longDiagonal' && d !== null) {
		a = d / 2;
	} else if (activeElementId === 'shortDiagonal' && s !== null) {
		a = s / Math.sqrt(3);
	} else if (activeElementId === 'circumcircleRadius' && R !== null) {
		a = R;
	} else if (activeElementId === 'apothem' && r !== null) {
		a = (2 * r) / Math.sqrt(3);
	} else if (activeElementId === 'area' && A !== null) {
		a = Math.sqrt((2 * A) / (3 * Math.sqrt(3)));
	} else if (activeElementId === 'perimeter' && P !== null) {
		a = P / 6;
	} else {
		// If no active input with a valid number, clear all and exit
		resetCalculator();
		return;
	}

	// If 'a' is not a valid number after initial calculation, clear all and exit
	if (isNaN(a) || a === null) {
		resetCalculator();
		return;
	}

	// Calculate all other values based on the determined 'a'
	d = 2 * a;
	s = Math.sqrt(3) * a;
	R = a;
	r = (Math.sqrt(3) / 2) * a;
	A = ((3 * Math.sqrt(3)) / 2) * a * a;
	P = 6 * a;

	// Helper function to update an input field, avoiding the active one
	const updateInputField = (id, value) => {
		if (document.activeElement.id !== id) {
			document.getElementById(id).value = value ? value.toFixed(2) : '';
		}
	};

	// Update all relevant input fields
	updateInputField('side', a);
	updateInputField('longDiagonal', d);
	updateInputField('shortDiagonal', s);
	updateInputField('circumcircleRadius', R);
	updateInputField('apothem', r);
	updateInputField('area', A);
	updateInputField('perimeter', P);
}

/**
 * Resets all input fields in the calculator to empty.
 */
function resetCalculator() {
	document.querySelectorAll('input').forEach((input) => (input.value = ''));
}

// Add event listeners after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
	// Attach input event listeners to all number input fields
	document.querySelectorAll('input[type="number"]').forEach((input) => {
		input.addEventListener('input', calculate);
	});

	// Attach click event listener to the reset button
	document.querySelector('button').addEventListener('click', resetCalculator);
});

function calculate(event) {
	let activeElementId = event.target.id;
	let a, d, s, R, r, A, P;

	const getInputValue = (id) => {
		let inputElement = document.getElementById(id);
		let valueStr = inputElement.value;
		valueStr = valueStr.replace(/[^0-9.,]/g, '');
		valueStr = valueStr.replace(',', '.');
		inputElement.value = valueStr;
		const parsedValue = parseFloat(valueStr);
		return isNaN(parsedValue) ? null : parsedValue;
	};

	a = getInputValue('side');
	d = getInputValue('longDiagonal');
	s = getInputValue('shortDiagonal');
	R = getInputValue('circumcircleRadius');
	r = getInputValue('apothem');
	A = getInputValue('area');
	P = getInputValue('perimeter');

	if (activeElementId === 'side' && a !== null) {
	} else if (activeElementId === 'longDiagonal' && d !== null) {
		a = d / 2;
	} else if (activeElementId === 'shortDiagonal' && s !== null) {
		a = s / Math.sqrt(3);
	} else if (activeElementId === 'circumcircleRadius' && R !== null) {
		a = R;
	} else if (activeElementId === 'apothem' && r !== null) {
		a = (2 * r) / Math.sqrt(3);
	} else if (activeElementId === 'area' && A !== null) {
		if (A < 0) {
			resetCalculator();
			return;
		}
		a = Math.sqrt((2 * A) / (3 * Math.sqrt(3)));
	} else if (activeElementId === 'perimeter' && P !== null) {
		a = P / 6;
	} else {
		resetCalculator();
		return;
	}

	if (isNaN(a) || a === null || a < 0) {
		resetCalculator();
		return;
	}

	d = 2 * a;
	s = Math.sqrt(3) * a;
	R = a;
	r = (Math.sqrt(3) / 2) * a;
	A = ((3 * Math.sqrt(3)) / 2) * (a * a);
	P = 6 * a;

	const updateInputField = (id, value) => {
		if (document.activeElement.id !== id) {
			document.getElementById(id).value =
				value !== null && value !== undefined && !isNaN(value)
					? value.toFixed(2)
					: '';
		}
	};

	updateInputField('side', a);
	updateInputField('longDiagonal', d);
	updateInputField('shortDiagonal', s);
	updateInputField('circumcircleRadius', R);
	updateInputField('apothem', r);
	updateInputField('area', A);
	updateInputField('perimeter', P);
}

function resetCalculator() {
	document.querySelectorAll('input').forEach((input) => (input.value = ''));
}

document.addEventListener('DOMContentLoaded', () => {
	document.querySelectorAll('input').forEach((input) => {
		input.addEventListener('input', calculate);
	});
	document.querySelector('button').addEventListener('click', resetCalculator);
});

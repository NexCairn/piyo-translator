document.addEventListener('DOMContentLoaded', () => {
    const inputText = document.getElementById('input-text');
    const outputText = document.getElementById('output-text');
    const btnEncode = document.getElementById('btn-encode');
    const btnDecode = document.getElementById('btn-decode');
    const btnCopy = document.getElementById('btn-copy');

    async function translate(action) {
        const text = inputText.value;
        if (!text) return;

        try {
            const response = await fetch('/api/translate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text, action }),
            });

            const data = await response.json();

            if (response.ok) {
                outputText.value = data.result;
            } else {
                alert(`Error: ${data.detail}`);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while communicating with the server.');
        }
    }

    btnEncode.addEventListener('click', () => translate('encode'));
    btnDecode.addEventListener('click', () => translate('decode'));

    btnCopy.addEventListener('click', () => {
        if (!outputText.value) return;
        navigator.clipboard.writeText(outputText.value).then(() => {
            const originalText = btnCopy.innerText;
            btnCopy.innerText = 'Copied!';
            setTimeout(() => {
                btnCopy.innerText = originalText;
            }, 2000);
        });
    });
});

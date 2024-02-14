
document.getElementById('title').addEventListener('input', handleInput);
document.getElementById('artist').addEventListener('input', handleInput);
document.getElementById('country').addEventListener('input', handleInput);

function handleInput(event) {
    const inputField = event.target;
    const suggestionsContainer = document.getElementById(`${inputField.id}Suggestions`);
    const identifier = inputField.id

    const inputValue = inputField.value.toLowerCase();
    if (!inputValue) {
        suggestionsContainer.innerHTML = '';
        return;
    }

    // Make an API request to get suggestions based on the input
    fetch(`/listings/api/records/?${identifier}=${inputValue}`)
        .then(response => response.json())
        .then(data => {
            const suggestions = data.suggestions;
            displaySuggestions(suggestions, inputField, suggestionsContainer, identifier);
        })
        .catch(error => {
            console.error('Error fetching suggestions:', error);
        });
}

function displaySuggestions(suggestions, inputField, suggestionsContainer, identifier) {
    console.log(suggestions)
    suggestionsContainer.innerHTML = '';
    suggestions.forEach(suggestion => {
        const suggestionElement = document.createElement('div');
        if (identifier==="country"){
            suggestionElement.textContent = suggestion.country;
        }
        else if(identifier==="title"){
            suggestionElement.textContent = suggestion.title;

        }
        else{
            suggestionElement.textContent = suggestion.name;
        }

        suggestionElement.addEventListener('click', () => {
            if (identifier==="country"){
                inputField.value = suggestion.country;}
            else if(identifier==="title"){
                inputField.value = suggestion.title;
            }
            else{inputField.value = suggestion.name;}
            suggestionsContainer.innerHTML = '';
        });
        suggestionsContainer.appendChild(suggestionElement);
    });
}


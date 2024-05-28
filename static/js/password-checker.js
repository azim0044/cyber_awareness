function submitInput() {
    const loadingTime = 1000;
    const categories = [
        '[*] Checking HaveIBeenPwned database',
        '[*] Checking password length and characters occurences',
        '[*] Global view of password characteristics',
        '[*] Looking for excessive occurences',
        '[*] Password Stregth'
    ];

    const outputContainer = document.getElementById('outputCategories');
    const password = document.getElementById('inputText').value;
    outputContainer.innerHTML = '';

    function loadCategory(index) {
        if (index < categories.length) {
            const category = categories[index];
            const outputCategory = document.createElement('div');
            outputCategory.className = 'output-category';
            const outputHeader = document.createElement('div');
            outputHeader.className = 'output-header';
            const categoryLabel = document.createElement('h5');
            categoryLabel.className = 'output-label';
            categoryLabel.textContent = category;
            const progressBarContainer = document.createElement('div');
            progressBarContainer.style.width = '20px';
            progressBarContainer.style.height = '20px';

            const progressBar = new ProgressBar.Circle(progressBarContainer, {
                strokeWidth: 5,
                color: '#007bff',
                trailColor: '#f8f9fa',
                trailWidth: 5,
                easing: 'easeInOut',
                duration: loadingTime,
                text: {
                    autoStyleContainer: false,
                },
                from: { color: '#007bff', width: 5 },
                to: { color: '#007bff', width: 5 },
                step: function (state, circle) {
                    circle.path.setAttribute('stroke', state.color);
                    circle.path.setAttribute('stroke-width', state.width);
                }
            });

            outputHeader.appendChild(categoryLabel);
            outputHeader.appendChild(progressBarContainer);
            outputCategory.appendChild(outputHeader);
            outputContainer.appendChild(outputCategory);

            setTimeout(() => {
                progressBar.destroy();

                if (index === 0) {
                    fetch('/haveibeenpwned-check', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ password: password }),
                    })
                        .then(response => response.json())
                        .then(data => {
                            const outputText = document.createElement('div');
                            outputText.className = 'output-text';
                            outputText.textContent = data.message;
                            outputText.style.color = data.color;
                            outputCategory.appendChild(outputText);
                            loadCategory(index + 1);
                        })
                        .catch((error) => {
                            console.error('Error:', error);
                        });
                } else if (index === 1) {
                    fetch('/passwordoccurance-check', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ password: password }),
                    })
                        .then(response => response.json())
                        .then(data => {
                            const outputText = document.createElement('div');
                            outputText.className = 'output-text';
                            const table = document.createElement('table');
                            table.className = 'my-table';
                            const thead = document.createElement('thead');
                            thead.className = 'my-thead';
                            thead.innerHTML = `<tr>
                     <th>Attribute</th>
                     <th>Value</th>
                   </tr>`;
                            table.appendChild(thead);
                            const tbody = document.createElement('tbody');
                            tbody.className = 'my-tbody';
                            const attributes = ['Password Length Status', 'Password Length', 'Special Characters', 'Numbers', 'Lower Characters', 'Upper Characters'];
                            const values = [
                                data.password_length_status,
                                data.password_length,
                                data["special characters"].split(': ')[1],
                                data.numbers.split(': ')[1],
                                data["lower characters"].split(': ')[1],
                                data["upper characters"].split(': ')[1]
                            ];
                            attributes.forEach((attribute, index) => {
                                const row = document.createElement('tr');
                                row.className = 'my-row';
                                row.innerHTML = `<td>${attribute}</td><td>${values[index]}</td>`;
                                tbody.appendChild(row);
                            });
                            table.appendChild(tbody);
                            outputText.appendChild(table);
                            outputCategory.appendChild(outputText);
                            loadCategory(index + 1);
                        })
                        .catch((error) => {
                            console.error('Error:', error);
                        });
                } else if (index === 2) {
                    fetch('/passwordoccurance-check', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ password: password }),
                    })
                        .then(response => response.json())
                        .then(data => {
                            const outputText = document.createElement('div');
                            outputText.className = 'output-text';
                            const table = document.createElement('table');
                            table.className = 'my-table';
                            const thead = document.createElement('thead');
                            thead.className = 'my-thead';
                            thead.innerHTML = `<tr>
                     <th>Character Type</th>
                     <th>Char Type Percentage In Password</th>
                   </tr>`;
                            table.appendChild(thead);
                            const tbody = document.createElement('tbody');
                            tbody.className = 'my-tbody';
                            const characterTypes = ['Digits characters', 'Special characters', 'Lowercase characters', 'Uppercase Characters'];
                            data.character_occurence_percentage.forEach((percentage, index) => {
                                const row = document.createElement('tr');
                                row.className = 'my-row';
                                row.innerHTML = `<td>${characterTypes[index]}</td><td>${percentage}</td>`;
                                tbody.appendChild(row);
                            });
                            const mixedCharacterTypesPercentageRow = document.createElement('tr');
                            mixedCharacterTypesPercentageRow.innerHTML = `<td>Mixed Character Types Percentage</td><td>${data.mixed_character_types_percentage}</td>`;
                            tbody.appendChild(mixedCharacterTypesPercentageRow);
                            table.appendChild(tbody);
                            outputText.appendChild(table);
                            outputCategory.appendChild(outputText);
                            loadCategory(index + 1);
                        })
                        .catch((error) => {
                            console.error('Error:', error);
                        });
                } else if (index === 3) {
                    fetch('/passwordoccurance-check', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ password: password }),
                    })
                        .then(response => response.json())
                        .then(data => {
                            const outputText = document.createElement('div');
                            outputText.className = 'output-text';
                            const table = document.createElement('table');
                            table.className = 'my-table';
                            const thead = document.createElement('thead');
                            thead.className = 'my-thead';
                            thead.innerHTML = `<tr>
                         <th>Attribute</th>
                         <th>Value</th>
                       </tr>`;
                            table.appendChild(thead);
                            const tbody = document.createElement('tbody');
                            tbody.className = 'my-tbody';
                            const row = document.createElement('tr');
                            row.className = 'my-row';
                            row.innerHTML = `<td>Excessive Occurrences</td><td>${data.excessive_occurences}</td>`;
                            tbody.appendChild(row);
                            table.appendChild(tbody);
                            outputText.appendChild(table);
                            outputCategory.appendChild(outputText);
                            loadCategory(index + 1);
                        })
                        .catch((error) => {
                            console.error('Error:', error);
                        });
                } else if (index === 4) {
                    fetch('/passwordentropy-check', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ password: password }),
                    })
                        .then(response => response.json())
                        .then(data => {
                            // Create a div element for the output text
                            const outputText = document.createElement('div');
                            outputText.className = 'output-text';

                            // Create a table for the result
                            const table = document.createElement('table');
                            table.className = 'my-table';

                            // Create the table header
                            const thead = document.createElement('thead');
                            thead.className = 'my-thead';
                            thead.innerHTML = `<tr>
                            <th>Attribute</th>
                            <th>Value</th>
                        </tr>`;
                            table.appendChild(thead);

                            // Create the table body
                            const tbody = document.createElement('tbody');
                            tbody.className = 'my-tbody';

                            // Create a row for the message with specified color
                            const row = document.createElement('tr');
                            row.className = 'my-row';
                            row.innerHTML = `<td>Message</td><td style="color: ${data.color}; font-weight:bold;">${data.message}</td>`;
                            tbody.appendChild(row);

                            // Append the body to the table
                            table.appendChild(tbody);

                            // Append the table to the output text
                            outputText.appendChild(table);

                            // Append the output text to the designated output area
                            outputCategory.appendChild(outputText);

                            // Continue with the next step (assuming loadCategory is defined)
                            loadCategory(index + 1);
                        })
                        .catch((error) => {
                            console.error('Error:', error);
                        });
                }

            }, loadingTime);

            progressBar.animate(1);
        }
    }

    loadCategory(0);
}

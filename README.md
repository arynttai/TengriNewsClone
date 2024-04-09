### Project README

This repository contains code for a web scraping and HTML modification application.

### Setup Instructions for Mentors

1. Clone the repository:
    ```bash
    git clone https://github.com/arynttai/tengri_news
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python main.py
    ```

### Design and Development Process

#### Approach:
The application focuses on web scraping and modifying HTML content. Key steps involved in the process include:
- Sending HTTP requests to the target URL.
- Parsing HTML content using BeautifulSoup.
- Modifying URLs in HTML attributes.
- Writing the updated HTML content to a file.

#### Unique Approaches/Methodologies:
1. **Modular Design**: The application is structured into functions for clarity and maintainability.
2. **Configurable URL Handling**: It handles various types of URLs and updates them appropriately.
3. **Error Handling**: Robust error handling ensures the application gracefully handles failures.

### Compromises and Known Issues

- **Compromises**: One compromise made during development is the assumption of consistent HTML structure for effective parsing and modification.
  
- **Known Issues**: 
    - The application currently handles only simple cases of URL modification. Complex scenarios or dynamic content may not be fully supported.
    - Error handling could be improved for more detailed error messages and better user guidance.

### Feedback and Contributions

Feedback and contributions are welcome! Feel free to submit a pull request or open an issue for any suggestions, bug reports, or improvements.

### Authors

This project was developed by [Arynttai](https://github.com/arynttai).

### Hosted Website

The project is live and can be viewed [here](https://arynttai.github.io/TengriNewsClone/).




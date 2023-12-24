# Judo Theory Web Application

## Note
This web application is in early development and I list plans here. I do not promise I will finish this but I will do my best

## Overview

This Flask web application serves as a comprehensive resource for Judo theory, providing users with access to educational content, tutorials, quizzes, and interactive learning materials. Whether you are a beginner looking to learn the basics or an experienced practitioner aiming to deepen your understanding, this platform is designed to support your learning journey.

## Planned Features

- **Interactive Tutorials**: :negative_squared_cross_mark: Step-by-step guides and tutorials to help users learn different Judo techniques and theories.
- **Quizzes**: :white_check_mark: Test your knowledge with quizzes tailored to different skill levels.
- **Video Demonstrations**: :negative_squared_cross_mark: Access to a library of video demonstrations showcasing various Judo techniques.
- **Progress Tracking**: :negative_squared_cross_mark: Users can track their learning progress and revisit topics as needed.
- **Responsive Design**: :negative_squared_cross_mark: Accessible on both desktop and mobile devices.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Fattigman/judo.git
   cd judo
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```
   python init_db.py
   ```

5. Start the application:
   ```
   flask run
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

Navigate to the application's URL in your web browser and start exploring the Judo theory materials and interactive lessons. You can register for an account to track your progress.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find a bug, please open an issue or submit a pull request.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or further assistance, please contact the project maintainers at [jacob.karlstrom@gmail.com](mailto:jacob.karlstrom@gmail.com).

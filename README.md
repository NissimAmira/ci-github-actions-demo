# CI GitHub Actions Demo

This project demonstrates CI/CD implementation using GitHub Actions with Python applications. It includes comprehensive testing workflows, scheduled builds, and matrix build strategies.

## Project Structure

```
ci-github-actions-demo/
├── main.py              # Core Python functions with mathematical operations
├── test_main.py         # Comprehensive unit tests using unittest
├── requirements.txt     # Python dependencies
└── .github/workflows/   # GitHub Actions workflow definitions
    ├── run_tests.yml    # Multi-version Python testing workflow
    └── scheduled_build.yml # Daily scheduled build workflow
```

## Features

### Core Functions (`main.py`)
- `add_numbers(a, b)` - Adds two numbers with support for integers and floats
- `is_even(number)` - Checks if a number is even, handles positive and negative integers
- `calculate_factorial(n)` - Calculates factorial with input validation and error handling

### Test Suite (`test_main.py`)
Comprehensive test coverage including:
- Basic functionality tests
- Edge cases (zero, negative numbers, floats)
- Error handling validation
- Exception testing for invalid inputs

## GitHub Actions Workflows

### 1. Run Tests Workflow (`run_tests.yml`)
**Triggers:**
- Push to `main` branch
- Manual dispatch via GitHub UI

**Features:**
- **Matrix Build Strategy**: Tests across Python versions 3.7, 3.8, 3.9, and 3.10
- **Platform**: Ubuntu 22.04
- **Caching**: pip cache enabled for faster builds
- **Steps**:
  1. Checkout repository code
  2. Setup Python environment with matrix version
  3. Upgrade pip to latest version
  4. Install project dependencies
  5. Run unit tests with verbose output

### 2. Scheduled Build Workflow (`scheduled_build.yml`)
**Triggers:**
- **Cron Schedule**: Daily at midnight UTC (`0 0 * * *`)
- Manual dispatch via GitHub UI

**Features:**
- Automated daily builds to catch integration issues
- Simple build validation
- Platform: Ubuntu Latest

## Tasks Implemented

### Task 1: Basic CI Setup
- Created initial GitHub Actions workflow
- Implemented Python environment setup
- Added basic test execution

### Task 2: Test Integration
- Integrated comprehensive unit testing
- Added proper Python dependency management
- Implemented test result reporting

### Task 3: Cron Scheduling
- Added scheduled workflow for daily builds
- Implemented workflow_dispatch for manual triggers
- Created separate build validation process

### Task 4: Matrix Builds
- Implemented matrix build strategy for multiple Python versions
- Added pip caching for performance optimization
- Enhanced workflow naming and organization

## Getting Started

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Local Development
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `python -m unittest -v`
4. Execute main program: `python main.py`

### CI/CD Pipeline
The project automatically runs tests on every push to the main branch and provides daily scheduled builds to ensure code quality and catch potential issues early.

## Workflow Status
- ✅ Multi-version Python testing (3.7-3.10)
- ✅ Automated dependency management
- ✅ Daily scheduled builds
- ✅ Manual workflow dispatch
- ✅ Comprehensive test coverage
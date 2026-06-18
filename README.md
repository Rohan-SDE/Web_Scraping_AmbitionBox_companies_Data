# AmbitionBox Web Scraper

A Python web scraper that extracts company information from AmbitionBox.com, including ratings, reviews, job openings, salary data, and company details.

## Overview

This project scrapes company information from [AmbitionBox](https://www.ambitionbox.com/), a platform that provides employee reviews, company ratings, salaries, and job information.

## Features

- **Company Name**: Extract company names
- **Ratings**: Scrape company ratings
- **Reviews**: Collect number of reviews
- **Services/Location**: Get service types and locations
- **Jobs**: Extract number of job openings
- **Salaries**: Collect salary information

## Requirements

- Python 3.x
- pandas
- requests
- beautifulsoup4
- lxml

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Web-Scraping
```

2. Install required dependencies:
```bash
pip install pandas requests beautifulsoup4 lxml
```

## Usage

Run the scraper:
```bash
python AmbitionBox_Scraped_data.py
```

The script will:
1. Fetch company data from AmbitionBox
2. Parse HTML content using BeautifulSoup
3. Extract relevant company information
4. Store data in a pandas DataFrame
5. Display the collected data

## Output

The script generates a DataFrame containing:
- **Name**: Company name
- **Ratings**: Company rating
- **Reviews**: Number of reviews
- **Services/Location**: Service type and location
- **Jobs**: Number of open positions
- **Salary**: Salary information

## Project Structure

```
Web-Scraping/
├── AmbitionBox_Scraped_data.py  # Main scraper script
└── README.md                     # Project documentation
```

## Legal Disclaimer

This scraper is for educational purposes only. Please ensure you comply with:
- The website's Terms of Service
- robots.txt guidelines
- Local laws and regulations regarding web scraping

Always check the website's policies before scraping.

## Notes

- The current implementation scrapes page 1 only (can be extended to multiple pages)
- User-Agent header is included to identify requests properly
- Error handling is implemented for missing ratings tags

## Future Enhancements

- [ ] Multi-page scraping
- [ ] Data export to CSV/Excel
- [ ] Error handling and logging
- [ ] Rate limiting to be respectful to the server
- [ ] Async requests for faster scraping
- [ ] Data validation and cleaning

## License

This project is for educational and personal use only.

## Contributing

Feel free to submit issues and enhancement requests!

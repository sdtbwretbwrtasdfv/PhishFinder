# PhishFinder

This Python script checks if a given word is similar to any words from a list stored in a file. It utilizes the Levenshtein distance algorithm to compare similarities between strings. The similarity is determined by a ratio calculated from the Levenshtein distance, and any word with a ratio higher than or equal to 0.8 is considered a match.
The purpose of this tool is to identify potential phishing domains by comparing a given domain name against a list of known phishing domains. It can also be used to find similar words or phrases for a variety of purposes.
This script is designed to be flexible and can easily be integrated into a Security Operations Center (SOC) system such as ArcSight. Furthermore, you can automate the process by incorporating daily data dumps from phishing detection websites like https://domains-monitor.com. By doing this, your SOC can effectively monitor for phishing activity and quickly detect potential threats.
With a daily automated update, you'll have the most recent data at your disposal, allowing your system to keep up with the fast-paced and ever-changing landscape of online threats. This feature, in conjunction with ArcSight's robust capabilities, can significantly enhance your cybersecurity defenses and overall system integrity.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

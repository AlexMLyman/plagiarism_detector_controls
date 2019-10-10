# plagiarism_detector_controls
Program to create control documents with certain degrees of similarity, intended for use testing plagiarism detectors.

In order to test plagiarism detecting software, control documents are needed where a fixed percent of each document was "plagiarized" from, or matching a second document. The documents are chunked into 10 equal sections, and each of those chunks has n percent replaced with an equally sized chunk from a corresponding chunk in the second document. This creates documents that are 0%, 1%, 2%, 5%, 10%, 25%, 50%, and 100% similar (See PNG in repository for a visual representation). The output documents are all 10000 words long. 
The program needs two text files as input at least 10000 words in length to create controls. 
Books at Project Gutenberg are ideal for this purpose https://www.gutenberg.org

Sample files, created from James Joyce's Ulysses and Herman Melville's Moby Dick are provided.

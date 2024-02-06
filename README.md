# csv2yml converter

> [!note] 
> CSV2YML converter is meant to be a script that is for a very specific use case. In this case we feed python a table `.csv` file and itll spit out 5 fields auto filled with their respective information.  Below is a diagram describing how this works.

```mermaid
graph TD;
    A[Start] --> B(Define csv_file_path and yaml_file_path);
    B --> C{Define csv_to_yaml function};
    C --> D[Open CSV file];
    D --> E[Read CSV data];
    E --> F[Prepare data for YAML];
    F --> G[Write YAML data to file];
    G --> H[End];
    H --> I[Example usage];
    I --> D;
```

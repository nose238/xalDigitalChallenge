import pandas as pd
df = pd.read_csv("/code/Sample.csv")
df = df[(df.state.str.len() == 2)] # Validate rows which len(state) == 2 
## Add necessary validatios to evaluate fields and clean Sample.csv
df.to_csv("SampleCleaned.csv", index = False)
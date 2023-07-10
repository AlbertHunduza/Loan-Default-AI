library(readr)

# Load train.csv
train_data <- read_csv("train.csv")

# Load test.csv
test_data <- read_csv("test.csv")

# Combine the datasets
combined_data <- bind_rows(train_data, test_data)

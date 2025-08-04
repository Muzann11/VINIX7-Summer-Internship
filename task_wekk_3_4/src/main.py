import pandas as pd
import os
from preprocessing_pipe import preprocess_description
from wordCloud import generate_wordcloud
import matplotlib.pyplot as plt

# Path input
input_path = os.path.join("data", "postings.csv")

# Pastikan folder output ada
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Output file paths
output_desc_path = os.path.join(output_dir, "wordcloud_description.png")
output_skills_path = os.path.join(output_dir, "wordcloud_skills_cleaned.png")

# Load data
df = pd.read_csv(input_path)

# Validasi kolom
required_columns = ['description', 'skills_desc']
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Kolom '{col}' tidak ditemukan dalam dataset.")


# Wordcloud untuk kolom description
processed_description = preprocess_description(df, 'description')
wordcloud_desc = generate_wordcloud(processed_description)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_desc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.savefig(output_desc_path, format='png')
plt.close()


# Wordcloud untuk kolom skills_desc
processed_skills = preprocess_description(df, 'skills_desc')
wordcloud_skills = generate_wordcloud(processed_skills)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_skills, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.savefig(output_skills_path, format='png')
plt.close()

# print(f"Wordcloud deskripsi pekerjaan disimpan di: {output_desc_path}")
print(f"Wordcloud skill disimpan di: {output_skills_path}")

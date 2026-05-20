base_text = "Error: the system failed. This error must be fixed."
clean_text = base_text.replace("error", "advertencia").replace("Error", "Advertencia")
print("Original text:", base_text)
print("Corrected text:", clean_text)
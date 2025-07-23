from sklearn.metrics import precision_score, recall_score, f1_score

def evaluate_model(relevant_chunks, ground_truth):
    """
    Evaluate the model's response using precision, recall, and F1-score.
    - relevant_chunks: The chunks returned by the model.
    - ground_truth: The actual correct answer or expected chunk.

    Returns precision, recall, and F1 score.
    """
    y_true = [1 if chunk in ground_truth else 0 for chunk in relevant_chunks]
    y_pred = [1] * len(relevant_chunks) 

    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    
    return precision, recall, f1

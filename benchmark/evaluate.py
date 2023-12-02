from implicit.evaluation import precision_at_k, mean_average_precision_at_k, ndcg_at_k


def evaluate(model, train_users_sparse, test_users_sparse):
    """
    Evaluate the performance of a movie recommendation model using Precision@k, MAP@k, 
    and NDCG@k metrics for k=10.
    
    Parameters:
    model: The movie recommendation model to be evaluated.
    train_users_sparse: The sparse matrix with training user-item interactions.
    test_users_sparse: The sparse matrix with test user-item interactions.
    
    Returns:
    tuple: A tuple containing the Precision@10, mean average precision@10, and NDCG@10 scores.
    """
    
    p10 = precision_at_k(model, 
                         train_users_sparse, 
                         test_users_sparse, 
                         K=10, 
                         show_progress=False)
    
    map10 = mean_average_precision_at_k(model, 
                                        train_users_sparse, 
                                        test_users_sparse, 
                                        K=10, 
                                        show_progress=False)
    ndcg10 = ndcg_at_k(model, 
                       train_users_sparse, 
                       test_users_sparse, 
                       K=10, 
                       show_progress=False)
    
    print(f'Precision@10={p10:.4f}, MAP@10={map10:.4f}, NDCG@10={ndcg10:.4f}')
    
    return p10, map10, ndcg10

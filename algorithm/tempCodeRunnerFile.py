# 假设现在有一个新用户，我们可以利用训练好的模型为他推荐电影
# new_user_id = 3
# # 构建一个新用户的观影记录
# new_user_history = torch.LongTensor([[new_user_id, movie_id.item()] for movie_id in movie_ids_tensor])
# # 基于观影记录预测新用户对电影的评分
# predicted_ratings = model(new_user_history)
# # 从预测的评分中挑选出前几部评分最高的电影作为推荐
# top_indices = predicted_ratings.argsort(descending=True)[:5]
# top_movie_ids = movie_ids_tensor[top_indices].tolist()

# print("推荐给新用户的电影ID：", top_movie_ids)

from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

# In-memory database to store movie reviews
movie_reviews = [
    {"id": 1, "title": "The Shawshank Redemption", "review": "A timeless masterpiece."},
    {"id": 2, "title": "The Godfather", "review": "A classic for a reason."},
]

# Serve the frontend
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# 1. Retrieve all movie reviews
@app.route('/reviews', methods=['GET'])
def get_reviews():
    return jsonify(movie_reviews), 200

# 2. Create a new movie review
@app.route('/reviews', methods=['POST'])
def create_review():
    new_review = request.get_json()
    if not new_review:
        return jsonify({"error": "Missing JSON in request body"}), 400
    new_review['id'] = len(movie_reviews) + 1
    movie_reviews.append(new_review)
    return jsonify({"message": "Review added successfully", "review": new_review}), 201

# 3. Update an existing movie review
@app.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    for i, review in enumerate(movie_reviews):
        if review['id'] == review_id:
            updated_data = request.get_json()
            movie_reviews[i].update(updated_data)
            return jsonify({"message": "Review updated successfully", "review": movie_reviews[i]}), 200
    return jsonify({"error": "Review not found"}), 404

# 4. Delete a movie review
@app.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    for i, review in enumerate(movie_reviews):
        if review['id'] == review_id:
            del movie_reviews[i]
            return jsonify({"message": "Review deleted successfully"}), 200
    return jsonify({"error": "Review not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
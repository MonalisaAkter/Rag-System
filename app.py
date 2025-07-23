from flask import Flask, request, jsonify
from query_system import query_rag_system, generate_answer

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    user_query = request.json.get('query')
    
  
    relevant_chunks = query_rag_system(user_query)
    answer = generate_answer(relevant_chunks)
    
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)

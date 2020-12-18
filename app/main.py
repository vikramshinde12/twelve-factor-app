"""The module to interact with employee details.
"""

import os
from flask import Flask, request, jsonify
from google.cloud import firestore

app = Flask(__name__)


@app.route('/<employee_id>', methods=['GET'])
def get_emmployee(employee_id):
    """ Retrieves employee details.

        Args:
            employee_id
        Returns:
            Employee details : If user exists
            404: if

                * User does not exist
        Raises:

            TypeError: If a keyword other than ``client`` is used.
        """
    client = firestore.Client()
    doc_ref = client.collection(u'employee').document(u'{}'.format(employee_id))
    doc = doc_ref.get()
    if doc.to_dict():
        response = jsonify(doc.to_dict())
        response.status_code = 200
    else:
        response = jsonify({
            'httpResponseCode': '404',
            'errorMessage': 'User does not exist'
        })
        response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

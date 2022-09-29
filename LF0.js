exports.handler = async (event) => {
    // TODO implement
    const response = {
        "messages": [
    {
      "type": "unstructured",
      "unstructured": {
        "id": "string",
        "text": "Application under development. Search functionality will be implemented in Assignment 2.",
        "timestamp": "string"
      }
    }
  ]
    };
    return response;
};

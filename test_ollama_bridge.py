import unittest
from unittest.mock import patch, MagicMock
import requests

from ollama_bridge import llamar_a_ollama

class TestLlamarAOllama(unittest.TestCase):

    @patch('ollama_bridge.requests.post')
    def test_llamar_a_ollama_success(self, mock_post):
        # Happy path
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": "  hello world  "}
        mock_post.return_value = mock_response

        result = llamar_a_ollama("model", "prompt", "fase")

        mock_post.assert_called_once_with(
            "http://127.0.0.1:11434/api/generate",
            json={"model": "model", "prompt": "prompt", "stream": False},
            timeout=300
        )
        mock_response.raise_for_status.assert_called_once()
        self.assertEqual(result, "hello world")

    @patch('ollama_bridge.sys.exit')
    @patch('ollama_bridge.requests.post')
    def test_llamar_a_ollama_connection_error(self, mock_post, mock_exit):
        mock_post.side_effect = requests.exceptions.ConnectionError("Connection refused")

        llamar_a_ollama("model", "prompt", "fase")

        mock_exit.assert_called_once_with(1)

    @patch('ollama_bridge.requests.post')
    def test_llamar_a_ollama_timeout(self, mock_post):
        mock_post.side_effect = requests.exceptions.Timeout("Timeout")

        result = llamar_a_ollama("model", "prompt", "fase")

        self.assertIsNone(result)

    @patch('ollama_bridge.requests.post')
    def test_llamar_a_ollama_exception(self, mock_post):
        mock_post.side_effect = Exception("Unexpected error")

        result = llamar_a_ollama("model", "prompt", "fase")

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

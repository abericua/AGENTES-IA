import unittest
from unittest.mock import patch, MagicMock
import urllib.error
import socket
import json

from asistente_gui import call_ollama, TIMEOUT_GLOBAL, URL_OLLAMA

class TestCallOllama(unittest.TestCase):

    @patch('asistente_gui.urllib.request.urlopen')
    def test_call_ollama_success(self, mock_urlopen):
        # Setup mock response
        mock_response = MagicMock()

        # Simulate lines of streaming JSON response
        mock_response.__iter__.return_value = iter([
            b'{"response": "Hello", "done": false}\n',
            b'\n',  # Empty line
            b'invalid json\n', # Invalid json
            b'{"response": " World", "done": false}\n',
            b'{"response": "!", "done": true}\n',
            b'{"response": " ignored", "done": false}\n', # Should be ignored because done=true was received
        ])

        # Make the mock act as a context manager
        mock_response.__enter__.return_value = mock_response

        mock_urlopen.return_value = mock_response

        # Call the function
        result = call_ollama("test_model", "test_prompt")

        # Verify the result
        self.assertEqual(result, "Hello World!")

        # Verify urlopen was called correctly
        mock_urlopen.assert_called_once()
        args, kwargs = mock_urlopen.call_args
        req = args[0]

        self.assertEqual(req.full_url, URL_OLLAMA)
        self.assertEqual(json.loads(req.data), {"model": "test_model", "prompt": "test_prompt", "stream": True})
        # Note: headers in Request are capitalized as Content-type internally, but let's just check standard dict
        self.assertEqual(req.get_header('Content-type'), "application/json")
        self.assertEqual(kwargs['timeout'], TIMEOUT_GLOBAL)

    @patch('asistente_gui.urllib.request.urlopen')
    def test_call_ollama_timeout(self, mock_urlopen):
        # Setup mock to raise a timeout error
        mock_urlopen.side_effect = urllib.error.URLError(socket.timeout("timeout"))

        # Verify the exception is propagated
        with self.assertRaises(urllib.error.URLError):
            call_ollama("test_model", "test_prompt")

if __name__ == '__main__':
    unittest.main()

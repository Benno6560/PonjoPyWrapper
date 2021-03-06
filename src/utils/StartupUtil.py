"""
Copyright 2022 Ben Petrillo. All rights reserved.

Project licensed under the MIT License: https://www.mit.edu/~amini/LICENSE.md

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.

All portions of this software are available for public use, provided that
credit is given to the original author(s).
"""

from requests import Response
from src.http.RequestFactory import RequestFactory

class StartupUtil:

    def __init__(self, key: str):
        self.key = key

    def isApiKeyValid(self) -> bool:
        response: Response = RequestFactory(self.key)\
            .setMethod("GET")\
            .setURL("https://app.ponjo.club/v1/covid")\
            .setHeaders({"Authorization": self.key})\
            .setTimeout(200)\
            .build()
        if response.status_code == 403:
            return False
        return True
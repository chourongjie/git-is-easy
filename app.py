{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "344fe18c-f5e3-47c9-9078-10d80b58984b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [01/Feb/2024 00:42:32] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [01/Feb/2024 00:42:35] \"POST / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [01/Feb/2024 00:42:40] \"POST / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [01/Feb/2024 00:42:42] \"POST / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [01/Feb/2024 00:42:45] \"POST / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [01/Feb/2024 00:42:47] \"POST / HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, render_template\n",
    "from textblob import TextBlob\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route(\"/\",methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "        return(render_template(\"index.html\"))\n",
    "\n",
    "@app.route(\"/result\",methods=[\"GET\",\"POST\"])\n",
    "def result():\n",
    "        i = request.form.get(\"i\")\n",
    "        r = TextBlob(i).sentiment\n",
    "        return(render_template(\"result.html\",r=r))\n",
    "\n",
    "@app.route(\"/end\",methods=[\"GET\",\"POST\"])\n",
    "def end():\n",
    "    return(render_template(\"end.html\"))\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fcadd045-4791-42f9-9d98-2bf868f318e8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

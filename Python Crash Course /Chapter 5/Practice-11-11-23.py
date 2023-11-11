{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPVELlubyqUC8Ptu4ASAoBd",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/BKnightHD/Python/blob/main/Python%20Crash%20Course%20/Chapter%205/Practice-11-11-23.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Practice 11/11/23"
      ],
      "metadata": {
        "id": "csP7vbZ2yyT3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "value = ['monkey', 'dragon', 'dog', 'cat', 'lion']\n",
        "'dog' in value # this returns True"
      ],
      "metadata": {
        "id": "UDQO1oJO0AEI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "peaky_blinders = ['tommy', 'aurther', 'johnny']\n",
        "woman = 'grace'\n",
        "woman in peaky_blinders # This tells us that grace is not in the peaky blinders list, returns false\n",
        "\n",
        "if woman not in peaky_blinders:\n",
        "  print(f\"Dont worry {woman.title()}, you're just a pedestrian, we aren't after you.\")"
      ],
      "metadata": {
        "id": "mlsV_c1Mz7xC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hVDsx7XDyk7g",
        "outputId": "30051316-d797-4e9f-9b4b-ee17a222bea8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Is car == to mazda?\n",
            "True\n",
            "Is car == to mercedes?\n",
            "False\n"
          ]
        }
      ],
      "source": [
        "# 5-1 Conditional Tests:\n",
        "car = 'mazda'\n",
        "print(\"Is car == to mazda?\")\n",
        "print(car == 'mazda')\n",
        "print(\"Is car == to mercedes?\")\n",
        "print(car == \"mercedes\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random # importing the random module which implements pseudo-random number generators for various distributions.\n",
        "people = ['jack', 'anthony', 'adam', 'christian', 'howard', 'cindy', 'alex', 'jordan', 'trinity', 'rachel', 'emily', 'allison', 'sarah', 'jillian', 'zach', 'troy']\n",
        "person = random.choice(people) #rnadom choice() method takes an arguments like a list, tuple, string, or range, and pass yoiurnlist as an argument, then it will reutnr a random element from it\n",
        "age_person = range(1,38)\n",
        "age = random.choice(age_person)\n",
        "if age < 16:\n",
        "  price = '$0'\n",
        "elif age < 18:\n",
        "  price = '$25'\n",
        "elif age < 21:\n",
        "  price = '$50'\n",
        "elif age < 30:\n",
        "  price = '$75'\n",
        "else:\n",
        "  price = '$100'"
      ],
      "metadata": {
        "id": "n6p4zJdw7Lsy"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "sVT5R4Pw9bYZ"
      },
      "execution_count": 9,
      "outputs": []
    }
  ]
}
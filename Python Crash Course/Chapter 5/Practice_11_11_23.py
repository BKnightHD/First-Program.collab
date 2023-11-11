{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOHyIB2bPTfHLd5Akqr+YQC",
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
        "<a href=\"https://colab.research.google.com/github/BKnightHD/Python/blob/main/Python/Python%20Crash%20Course/%20Chapter%205/Practice_11_11_23.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hVDsx7XDyk7g",
        "outputId": "6b887981-fb03-40d2-8219-b307aa7684ee"
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
    }
  ]
}
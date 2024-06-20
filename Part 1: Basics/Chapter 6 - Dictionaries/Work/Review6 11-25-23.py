{ 
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOOqglq8uURadFb+HGGlsHD",
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
        "<a href=\"https://colab.research.google.com/github/BKnightHD/Python-CC/blob/main/Untitled9.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "daH_iW4dfg_R",
        "outputId": "580fe72d-9769-43bc-9156-e70106b01223"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Green\n"
          ]
        }
      ],
      "source": [
        "# Reviewing dictionaries\n",
        "alien_0 = {'color': 'green'}\n",
        "print(alien_0['color'].title())"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "people = {\n",
        "    'alex': 'python',\n",
        "    'jordan': 'c++',\n",
        "    'eddie': 'java',\n",
        "    'aldin': 'scala',\n",
        "    'devin': 'r'\n",
        "    }\n",
        "\n",
        "for names, languages in people.items():\n",
        "  print(f\"{names.title()} likes {languages.title()}.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TAboQvpqgQVV",
        "outputId": "b8635974-3c60-4d32-d51e-5fa0b9fdb537"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Alex likes Python.\n",
            "Jordan likes C++.\n",
            "Eddie likes Java.\n",
            "Aldin likes Scala.\n",
            "Devin likes R.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Adding to a dictionary (good for looping)"
      ],
      "metadata": {
        "id": "Ql4XxTrdkvfL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "alien_0 = {\n",
        "    'color': 'green',\n",
        "    'points': 5\n",
        "    }\n",
        "print(alien_0)\n",
        "\n",
        "# Here we add new keys and items to the dictionary\n",
        "alien_0['x_position'] = 0\n",
        "alien_0['y position'] = 25\n",
        "\n",
        "print(alien_0)\n",
        "print('...\\n')\n",
        "\n",
        "# Starting with an empty dictionary\n",
        "person = {}\n",
        "stats = {\n",
        "    'name': 'brandon',\n",
        "    'height in inches': 70,\n",
        "    'race': 'african american',\n",
        "    'eye color': 'dark brown'\n",
        "}\n",
        "\n",
        "print(person)\n",
        "\n",
        "person = stats\n",
        "print(person)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dm5GQlE5jH3f",
        "outputId": "8c275e19-8134-4f85-cfd5-7c5f514a9643"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'color': 'green', 'points': 5}\n",
            "{'color': 'green', 'points': 5, 'x_position': 0, 'y position': 25}\n",
            "...\n",
            "\n",
            "{}\n",
            "{'name': 'brandon', 'height in inches': 70, 'race': 'african american', 'eye color': 'dark brown'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "alien_0 = {}\n",
        "\n",
        "alien_0['color'] = 'green'\n",
        "alien_0['points'] = 5\n",
        "\n",
        "print(alien_0)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iir95FeJkeWT",
        "outputId": "efd08c85-0308-4ced-e06a-3f777b739290"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'color': 'green', 'points': 5}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "YuIsAS9wmGaN"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
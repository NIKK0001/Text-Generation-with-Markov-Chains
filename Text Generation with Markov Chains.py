                                                                                                                                                                                                                                                             import random

class MarkovChainTextGenerator:
    def _init_(self, order=1):
        self.order = order
        self.model = {}

    def train(self, text):
        words = text.split()
        if len(words) < self.order:
            raise ValueError("Text is too short for the given order")

        for i in range(len(words) - self.order):
            key = tuple(words[i:i + self.order])
            next_word = words[i + self.order]

            if key not in self.model:
                self.model[key] = []
            self.model[key].append(next_word)

    def generate(self, length=100):
        if not self.model:
            raise ValueError("Model has not been trained")

        # Start with a random key
        current_key = random.choice(list(self.model.keys()))
        result = list(current_key)

        for _ in range(length - self.order):
            if current_key in self.model:
                next_word = random.choice(self.model[current_key])
                result.append(next_word)
                current_key = tuple(result[-self.order:])
            else:
                break

        return ' '.join(result)

# Example usage
if _name_ == "_main_":
    text = """Markov chains are mathematical systems that undergo transitions from one state to another within a finite state space. They are named after Andrey Markov, a Russian mathematician. Markov chains are used in various fields, including statistics, economics, and computer science."""

    generator = MarkovChainTextGenerator(order=2)
    generator.train(text)
    generated_text = generator.generate(length=50)
    print(generated_text)
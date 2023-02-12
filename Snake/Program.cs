using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SnakeGame
{
    class Program
    {
        static void Main(string[] args)
        {
            // Initialize variables for the game
            int x = 0, y = 0; // Coordinates of the snake's head
            int foodX = 10, foodY = 10; // Coordinates of the food
            string direction = "RIGHT"; // Direction the snake is moving
            int score = 0; // Score
            bool isGameOver = false; // Is the game over?
            List<int> snakeXs = new List<int>(); // List of X-coordinates for the snake's body
            List<int> snakeYs = new List<int>(); // List of Y-coordinates for the snake's body
            Random randomNumberGenerator = new Random(); // Declare a "Random" object for generating X-Y coordinates for the food

            // Game loop
            while (!isGameOver)
            {
                Console.Clear();

                // Draw the snake's body on the console window
                for (int i = 0; i < snakeXs.Count; i++)
                {
                    Console.SetCursorPosition(snakeXs[i], snakeYs[i]);
                    Console.Write("*");
                }

                // Draw the food on the console window
                Console.SetCursorPosition(foodX, foodY);
                Console.Write("@");

                // Display the score on the console window
                Console.SetCursorPosition(0, 0);
                Console.Write("Score: " + score);

                // Get user input for the direction
                ConsoleKeyInfo userInput = Console.ReadKey();
                if (userInput.Key == ConsoleKey.LeftArrow)
                {
                    direction = "LEFT";
                }
                else if (userInput.Key == ConsoleKey.RightArrow)
                {
                    direction = "RIGHT";
                }
                else if (userInput.Key == ConsoleKey.UpArrow)
                {
                    direction = "UP";
                }
                else if (userInput.Key == ConsoleKey.DownArrow)
                {
                    direction = "DOWN";
                }

                // Move the snake in the chosen direction
                if (direction == "RIGHT")
                {
                    x++;
                }
                else if (direction == "LEFT")
                {
                    x--;
                }
                else if (direction == "UP")
                {
                    y--;
                }
                else if (direction == "DOWN")
                {
                    y++;
                }

                // Check if the snake has hit the food
                if (x == foodX && y == foodY)
                {
                    // Increase the score
                    score++;

                    // Generate new coordinates for the food
                    foodX = randomNumberGenerator.Next(0, Console.WindowWidth);
                    foodY = randomNumberGenerator.Next(0, Console.WindowHeight);
                }

                                // Check if the snake has hit the boundaries of the console window
                if (x < 0 || x >= Console.WindowWidth || y < 0 || y >= Console.WindowHeight)
                {
                    isGameOver = true;
                    Console.WriteLine("Game Over! Your final score is " + score);
                }
                else
                {
                    // Add the new head coordinates to the snake's body lists
                    snakeXs.Add(x);
                    snakeYs.Add(y);

                    // Remove the tail coordinates from the snake's body lists
                    snakeXs.RemoveAt(0);
                    snakeYs.RemoveAt(0);
                }

                // Sleep for a short period of time to slow down the movement of the snake
                System.Threading.Thread.Sleep(100);
            }
        }
    }
}
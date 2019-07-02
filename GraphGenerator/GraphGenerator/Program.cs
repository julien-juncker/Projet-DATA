using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GraphGenerator
{
    class Program
    {
        static int cities = 20;
        static int Xmax = 1000;
        static int Ymax = 1000;
        static Random rnd = new Random();

        static void Main(string[] args)
        {
            Stopwatch s = new Stopwatch();
            s.Start();

            List<City> graph = new List<City>();
            for (int i = 0; i < cities; i++)
            {
                graph.Add(AddCity(graph, i));
            }

            int[,] matrix = new int[cities, cities];

            for (int i = 0; i < cities; i++)
            {
                for (int j = 0; j < cities; j++)
                {
                    matrix[i,j] =(j !=i) ?  GetDistance(graph[i], graph[j]) : 0;
                    Console.Write(matrix[i, j] + "  ");
                }
                Console.WriteLine();
            }

            string result = JsonConvert.SerializeObject(matrix, Formatting.Indented);

            string path = @"D:\Documents\Programmation\C#\GraphGenerator\GraphGenerator\result.json";

            using (StreamWriter sw = File.CreateText(path))
            {
                sw.WriteLine(result);
            }

            Console.Write(s.ElapsedMilliseconds);
            Console.ReadLine();
        }

        static City AddCity(List<City> graph, int id)
        {
            City c = new City()
            {
                ID = id
            };

            bool passed = false;

            while(!passed)
            {
                c.X = rnd.Next(0, Xmax);
                c.Y = rnd.Next(0, Ymax);

                if (graph.FindAll(city => city.X == c.X && city.Y == c.Y).Count == 0)
                {
                    passed = true;
                }
            }
            return c;
        }

        static private int GetDistance(City a, City b)
        {
            double distance = Math.Sqrt(Math.Pow(Math.Abs(a.X - b.X), 2) + Math.Pow(Math.Abs(a.Y - b.Y), 2));
            return Convert.ToInt32(distance);
        }
    }

    class City
    {
        public int ID { get; set; }
        public int X { get; set; }
        public int Y { get; set; }
    }
}

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
        static void Main(string[] args)
        {
            Stopwatch s = new Stopwatch();
            s.Start();

            int cities = 1000;
            List<City> graph = new List<City>();
            Random rnd = new Random();
            for (int i = 0; i < cities; i++)
            {
                graph.Add(AddCity(graph, i, rnd, cities));
            }

            for (int i = 0; i < cities; i++)
            {
                for (int y = 0; y < cities; y++)
                {
                    if (i != graph[y].ID)
                    {
                        graph[i].Neighbours.Add(new Neighbour()
                        {
                            City = graph[y].ID,
                            Distance = GetDistance(graph[i], graph[y])
                        }
                    );
                    }
                }
            }

            for (int i = 0; i < cities; i++)
            {

                graph[i].Neighbours = graph[i].Neighbours.OrderBy(n => n.Distance).ToList();
                graph[i].Neighbours.RemoveRange(10, cities - 11);
            }

            string result = JsonConvert.SerializeObject(graph, Formatting.Indented);

            string path = @"D:\Documents\Programmation\C#\GraphGenerator\GraphGenerator\result.json";

            using (StreamWriter sw = File.CreateText(path))
            {
                sw.WriteLine(result);
            }

            Console.Write(s.ElapsedMilliseconds);
            Console.ReadLine();
        }

        static City AddCity(List<City> graph, int id, Random rnd, int max)
        {
            City c = new City()
            {
                ID = id,
                Neighbours = new List<Neighbour>()
            };

            bool passed = false;

            while(!passed)
            {
                c.X = rnd.Next(0, max);
                c.Y = rnd.Next(0, max);

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
        public List<Neighbour> Neighbours { get; set; }
    }

    class Neighbour
    {
        public int City { get; set; }
        public int Distance { get; set; }
    }
}

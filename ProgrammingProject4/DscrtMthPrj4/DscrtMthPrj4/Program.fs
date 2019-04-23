// Learn more about F# at http://fsharp.org

open System

[<EntryPoint>]
let main argv =
    //Console.WriteLine(LinearRandom.GetAvg (100, 69., 71.))
    //Console.WriteLine(LinearRandom.GetAvg (100, 69.9, 70.1))
    Console.WriteLine(LinearRandom.GetReliableCount (69., 71.))
    Console.WriteLine(LinearRandom.GetReliableCount (69.9, 70.1))
    //Console.WriteLine(NormalDistribution.GetReliableCount NormalDistribution.BigRange)
    //Console.WriteLine(NormalDistribution.GetReliableCount NormalDistribution.SmallRange)
    Console.WriteLine(NormalDistribution.GetReliableCountDevTwo NormalDistribution.BigRange)
    Console.WriteLine(NormalDistribution.GetReliableCountDevTwo NormalDistribution.SmallRange)
    let key = Console.ReadKey true
    0 // return an integer exit code

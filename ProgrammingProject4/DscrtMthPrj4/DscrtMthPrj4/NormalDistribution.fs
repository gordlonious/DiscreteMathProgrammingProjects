module NormalDistribution

open System
open MathNet.Numerics.Distributions

// A normal distribution with a mean of 70 and a standard deviation of 0.5
let normaldevhalf = Normal.WithMeanStdDev (70., 0.5)

let normaldevtwo = Normal.WithMeanStdDev (70., 2.)

let BigRange = (69., 71.)

let SmallRange = (69.9, 70.1)

// Does the normal distribution sample almost always fall within the mean+stddev range?
let chanceBool range =

    let s = normaldevhalf.Sample ()

    s >= (fst range) && s <= (snd range)

let chanceBoolTwo range =

    let s = normaldevtwo.Sample ()

    s >= (fst range) && s <= (snd range)

// What does 'reliable' mean again? I'll simply exit when 10 samples in a row are within range
let GetReliableCount range =

    let rec get inTargetCount offTargetCount callsToChanceBoolCount =

        if inTargetCount = 10 
        then callsToChanceBoolCount
        else
            match chanceBool range with
            | true -> get (inTargetCount+1) offTargetCount (callsToChanceBoolCount+1)
            | false -> get 0 (offTargetCount+1) (callsToChanceBoolCount+1)

    get 0 0 0

let GetReliableCountDevTwo range =

    let rec get inTargetCount offTargetCount callsToChanceBoolCount =

        if inTargetCount = 10 
        then callsToChanceBoolCount
        else
            match chanceBoolTwo range with
            | true -> get (inTargetCount+1) offTargetCount (callsToChanceBoolCount+1)
            | false -> get 0 (offTargetCount+1) (callsToChanceBoolCount+1)

    get 0 0 0
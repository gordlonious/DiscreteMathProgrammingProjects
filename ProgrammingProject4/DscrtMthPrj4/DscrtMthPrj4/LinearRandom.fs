module LinearRandom

open System

let Target = 70

let chanceBool chance =

    let r = new Random()

    Seq.contains (r.Next 100) {0 .. chance}

let GetReliableCount (min:double, max:double):int =

    let rec get (inTargetCount:double, offTargetCount:double, callsToChanceBoolCount:int):int =

        let percentTrue = if callsToChanceBoolCount <> 0 then ((inTargetCount / (double callsToChanceBoolCount))*100.) else 0.

        if percentTrue >= min && percentTrue <= max
        then callsToChanceBoolCount
        else
            match chanceBool Target with
            | true -> get ((inTargetCount+1.), offTargetCount, (callsToChanceBoolCount+1))
            | false -> get (inTargetCount, (offTargetCount+1.), (callsToChanceBoolCount+1))

    get (0., 0., 0)

let GetAvg (sampleCount:int, min:float, max:float):float =

    let addReliable (count:int, getReliable):List<int> =

        let rec get (results:List<int>, count:int):List<int> =

            if count = 0 
            then results
            else
                get (((getReliable (min, max)) :: results) , (count-1))

        get (List.empty, count)

    let l = (addReliable (sampleCount, GetReliableCount))

    List.averageBy (fun el -> float el) l

    
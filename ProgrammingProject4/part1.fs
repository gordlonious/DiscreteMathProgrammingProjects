open System

let r = new Random()

let Target = 70

let chanceBool chance =

    Seq.contains (r.Next 100) {0 .. chance}

let getReliableCount (min:double, max:double):int =

    let rec get (inTargetCount:double, offTargetCount:double, callsToChanceBoolCount:int):int =

        let percentTrue = if callsToChanceBoolCount <> 0 then (inTargetCount / (double callsToChanceBoolCount)*100.) else 0.

        if percentTrue >= min && percentTrue <= max
        then callsToChanceBoolCount
        else
            match chanceBool Target with
            | true -> get ((inTargetCount+1.), offTargetCount, (callsToChanceBoolCount+1))
            | false -> get (inTargetCount, (offTargetCount+1.), (callsToChanceBoolCount+1))

    get (0., 0., 0)

printfn "%d" (getReliableCount(69., 71.))

printfn "%d" (getReliableCount(69.9, 71.1))
open System

let r = new Random()

let Target = 70

let chanceBool chance =

    Seq.contains (r.Next 100) {0 .. chance}

let getReliableCount min max =

    let rec get inTargetCount offTargetCount callsToChanceBoolCount min max =
        
        //printfn "%d %d" inTargetCount offTargetCount
        if offTargetCount <> 0 && (inTargetCount / offTargetCount) >= min && (inTargetCount / offTargetCount) <= max
        then callsToChanceBoolCount
        else
            match chanceBool Target with
            | true -> get (inTargetCount+1) offTargetCount (callsToChanceBoolCount+1) min max
            | false -> get inTargetCount (offTargetCount+1) (callsToChanceBoolCount+1) min max

    get 0 0 0 min max

printfn "%d" (getReliableCount 60 80)
//printfn "%d" (getReliableCount 69.9 71.1)
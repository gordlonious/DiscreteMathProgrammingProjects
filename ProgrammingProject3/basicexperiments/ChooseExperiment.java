package basicexperiments;
import java.util.stream.Stream;
import java.util.Collections;
import java.util.ArrayList;
import java.util.List;

public class ChooseExperiment {
	
	static int MAX_WEIGHT = 700;
	
	public static void main(String[] args)
	{
		// print out Experiments used if selected based on highest rating
		Collections.sort(Experiments.GetInstance().ExperimentsList, (Experiment e1, Experiment e2) -> e2.Rating - e1.Rating);
		
		System.out.println("Selected based on highest rating:");
		int currentWeight = 0;		
		for(Experiment e : Experiments.GetInstance().ExperimentsList)
		{
			if(currentWeight + e.Weight >= MAX_WEIGHT) break;
			
			currentWeight += e.Weight;
			
			System.out.println("    " + e.Name);
		}
		System.out.printf("    Total weight used: %d%n", currentWeight); 
	}
}
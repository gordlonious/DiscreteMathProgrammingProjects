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
		int cw1 = 0;
		int r1 = 0;
		for(Experiment e : Experiments.GetInstance().ExperimentsList)
		{
			if(cw1 + e.Weight >= MAX_WEIGHT) break;
			
			cw1 += e.Weight;
			r1 += e.Rating;
			
			System.out.println("    " + e.Name);
		}
		System.out.printf("    Total weight used: %d%n", cw1);
		System.out.printf("    TOTAL RATING: %d%n", r1);
		
		// print out Experiments used if lightest are used first
		Collections.sort(Experiments.GetInstance().ExperimentsList, (Experiment e1, Experiment e2) -> e1.Weight - e2.Weight);
		
		System.out.println("Selected based on lowest weight:");
		int cw2 = 0;
		int r2 = 0;
		for(Experiment e : Experiments.GetInstance().ExperimentsList)
		{
			if(cw2 + e.Weight >= MAX_WEIGHT) break;
			
			cw2 += e.Weight;
			r2 += e.Rating;
			
			System.out.println("    " + e.Name);
		}
		System.out.printf("    Total weight used: %d%n", cw2);
		System.out.printf("    TOTAL RATING: %d%n", r2);
		
		// print out Experiments used if the lowest weight/rating ratio is used first
		Collections.sort(Experiments.GetInstance().ExperimentsList, (Experiment e1, Experiment e2) -> e1.Weight/e1.Rating - e2.Weight/e2.Rating);
		
		System.out.println("Selected based on lowest weight/rating ratio");
		int cw3 = 0;
		int r3 = 0;
		for(Experiment e : Experiments.GetInstance().ExperimentsList)
		{
			if(cw3 + e.Weight >= MAX_WEIGHT) break;
			
			cw3 += e.Weight;
			r3 += e.Rating;
			
			System.out.println("    " + e.Name);
		}
		System.out.printf("    Total weight used: %d%n", cw3);
		System.out.printf("    TOTAL RATING: %d%n", r3);
	}
}
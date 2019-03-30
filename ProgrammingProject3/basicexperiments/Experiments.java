package basicexperiments;
import java.util.Arrays;
import java.util.List;
import java.util.Collection;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
//import java.util.stream;

public class Experiments {
	
	private Experiments()
	{
		ExperimentsList = List.of(
			new Experiment("Cloud Patterns", 36, 5),
			new Experiment("Solar Flares", 264, 9),
			new Experiment("Solar Power", 188, 6),
			new Experiment("Binary Stars", 203, 8),
			new Experiment("Relativity", 104, 8),
			new Experiment("Seed Viability", 7, 4),
			new Experiment("Sun Spots", 90, 2),
			new Experiment("Mice Tumors", 65, 8),
			new Experiment("Microgravity Plant Growth", 75, 5),
			new Experiment("Micrometeorites", 170, 9),
			new Experiment("Cosmic Rays", 80, 7),
			new Experiment("Yeast Fermentation", 27, 4)
		);
		
		ExperimentsByRating = new HashMap<>();
		
		for(Experiment e : ExperimentsList)
		{
			if(ExperimentsByRating.containsKey(e.Rating)) ExperimentsByRating.get(e.Rating).add(e);
			
			else ExperimentsByRating.put(e.Rating, new ArrayList(Arrays.asList(e)));
		}
	}
	
	public static Experiments GetInstance()
	{
		if (Instance == null)
		{
			Instance = new Experiments();
			return Instance;
		}
		else return Instance;
	}
	
	private static Experiments Instance;
	
	public List<Experiment> ExperimentsList;
	
	public Map<Integer, List<Experiment>> ExperimentsByRating;
}
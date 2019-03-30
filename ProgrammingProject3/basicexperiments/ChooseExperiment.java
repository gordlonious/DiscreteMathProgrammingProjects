package basicexperiments;

public class ChooseExperiment {
	
	public static void main(String[] args)
	{
		System.out.println(Experiments.GetInstance().ExperimentsByRating.get(5).get(0).Name);
	}
}
package Yoon.Ex05;

import java.io.*;
import java.util.ArrayList;

public class ExamFileReader {
	public ArrayList<ExamDao> reader() {
		ArrayList<ExamDao> arr = new ArrayList<ExamDao>();
		String path = System.getProperty("user.dir");
		String s = null;
		
		try {
			BufferedReader in = new BufferedReader(new FileReader(path  + "/src/Ex05/ExamFile.txt"));
			while ((s = in.readLine()) != null) {
				//System.out.println(s);
				/**
				 * To-Do
				 */
				String[] line = s.split(" ");
				ExamDao dao = new ExamDao();
				dao.setKorean_Score(Integer.parseInt(line[0]));
				dao.setEnglish_Score(Integer.parseInt(line[1]));
				dao.setMath_Score(Integer.parseInt(line[2]));
				dao.setName(line[3]);
				arr.add(dao);
			}
			in.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return arr;
	}
}

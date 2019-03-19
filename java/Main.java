// import java.io.BufferedReader;
// import java.io.IOException;
// import java.io.InputStreamReader;

// public class PowerShellCommand {

//  public static void main(String[] args) throws IOException {

//   //String command = "powershell.exe  your command";
//   //Getting the version
//   String command = "cmd.exe /C echo Hello DanDan";
//   // Executing the command
//   Process powerShellProcess = Runtime.getRuntime().exec(command);
//   // Getting the results
//   powerShellProcess.getOutputStream().close();
//   String line;
//   System.out.println("Standard Output:");
//   BufferedReader stdout = new BufferedReader(new InputStreamReader(
// 	powerShellProcess.getInputStream()));
//   while ((line = stdout.readLine()) != null) {
//    System.out.println(line);
//   }
//   stdout.close();
//   System.out.println("Standard Error:");
//   BufferedReader stderr = new BufferedReader(new InputStreamReader(
// 	powerShellProcess.getErrorStream()));
//   while ((line = stderr.readLine()) != null) {
//    System.out.println(line);
//   }
//   stderr.close();
//   System.out.println("Done");

//  }

// }

























/**
  * This is the source file for the Java GUI program
  * Its very basic, but gets the job done.
  * I do however recommend the alternative command line python program
  *
  * @author Daniel J. Finnegan
  * @date July 2017
  */

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.List; // For the arraylist shuffling
import java.util.ArrayList;
import java.util.Date;
import java.util.Collections;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.PrintWriter;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;
import java.io.File;
import java.util.Calendar;
import javax.swing.filechooser.FileNameExtensionFilter;

// Swing Program Template
@SuppressWarnings("serial")
public class Main extends JFrame {
   // Name-constants to define the various dimensions
   public static final int WINDOW_WIDTH = 480;
   public static final int WINDOW_HEIGHT = 240;
   public static final int NUMBER_INPUT_COLUMNS = 1;

   public static final int TEXT_PANEL_WIDTH = 480;
   public static final int TEXT_PANEL_HEIGHT = 200;
   public static final int BUTTON_PANEL_WIDTH = 100;
   public static final int BUTTON_PANEL_HEIGHT= 20;
   private static final String FRAME_TITLE = "Run bib tool";

   ////////////////////////////////////////////////////////////////////

   // All of the UI elements

   private JPanel textPanel;
   private JPanel buttonPanel;
   private JButton createButton;

   // Allocate the UI components
   public static final String[] programIDs = {"Bib2CSV", "CSV2Bib"};
   private JComboBox<String> program;
   private JSpinner cuttoffYear;
   private JCheckBox dumpKeywords;
   private boolean dumpingKeywordsBool = false;
   private final JTextField inputFileTextField = new JTextField ();
   private final JTextField outputDirectoryTextField = new JTextField ();

   ////////////////////////////////////////////////////////////////////
 
   /** Constructor to setup the UI components */
   public Main() {
	  // Create the GUI
	  createAndShowGUI();

	  // Add the custom action listener for the create button
	  createButton.addActionListener(new ActionListener() {

		 @Override
		 public void actionPerformed(ActionEvent ev) {
		 	try {
				// // String command = "cmd.exe /C echo Hello DanDan";
				// String command = "cmd.exe /C make.bat";

		 		/**
		 		  * Based on the GUI values, we call the bibtex2csv batch files
		 		  */
		 		String programToRun = programIDs[program.getSelectedIndex()];
		 		String inputFile = inputFileTextField.getText ();
		 		String outputDirectory = outputDirectoryTextField.getText ();

		 		// Debugging
		 		// System.out.println ("Program: " + programToRun);
		 		// System.out.println ("Input: " + inputFile);
		 		// System.out.println ("Output: " + outputDirectory);
		 		// System.out.println ("Dumping keywords: " + dumpingKeywordsBool);

		 		// go ahead and prepare the command
		 		StringBuilder sb = new StringBuilder ();
		 		sb.append ("cmd.exe /C");
		 		sb.append (" python bib2xyz.py");
		 		if (programToRun.equals ("Bib2CSV")) {
		 			sb.append (" --input-format=bibtex");
		 			sb.append (" --output-format=csv");
		 			sb.append (" --output-file=output.csv");
		 		}
		 		else {
		 			sb.append (" --input-format=csv");
		 			sb.append (" --output-format=bibtex");
		 			sb.append (" --output-file=output.bib");
		 		}

		 		sb.append (" --output-dir=\"" + outputDirectory + "\"");
		 		if (dumpingKeywordsBool) {
		 			sb.append (" --dump-keywords");
		 		}

		 		sb.append (" \"" + inputFile + "\"");

		 		System.out.println ("Command: " + sb.toString ());

		 		// throw new IOException ();

				// Executing the command
				Process powerShellProcess = Runtime.getRuntime().exec(sb.toString ());
				// Getting the results
				powerShellProcess.getOutputStream().close();
				String line;
				System.out.println("Standard Output:");
				BufferedReader stdout = new BufferedReader(new InputStreamReader(
				powerShellProcess.getInputStream()));
				while ((line = stdout.readLine()) != null) {
				System.out.println(line);
				}
				stdout.close();
				System.out.println("Standard Error:");
				BufferedReader stderr = new BufferedReader(new InputStreamReader(
				powerShellProcess.getErrorStream()));
				while ((line = stderr.readLine()) != null) {
				System.out.println(line);
				}
				stderr.close();
				System.out.println("Done");
		 	}
		 	catch (IOException iex) {

		 	}
		 }

	  });      
   }

   /**
	 * Creates the high level GUI
	 */
   public void createAndShowGUI() {
	  textPanel = new JPanel();
	  buttonPanel = new JPanel();
	  createButton = new JButton("Convert");

	  // Content-pane sets layout
	  textPanel.setLayout(new BoxLayout(textPanel, BoxLayout.Y_AXIS));
	  // textPanel.setLayout(new BorderLayout());
	  textPanel.setPreferredSize(new Dimension(TEXT_PANEL_WIDTH, TEXT_PANEL_HEIGHT));
	  buttonPanel.setLayout(new BorderLayout());
	  buttonPanel.setPreferredSize(new Dimension(BUTTON_PANEL_WIDTH, BUTTON_PANEL_HEIGHT));
	  // setLayout(new BoxLayout(getContentPane(), BoxLayout.Y_AXIS));
	  setLayout(new BorderLayout());

	  // Create the actual panels
	  createDataPanel();
	  buttonPanel.add(createButton, BorderLayout.CENTER);

	  // Add the elements, with a seperator
	  add(Box.createHorizontalGlue());
	  add(textPanel, BorderLayout.PAGE_START);
	  add(Box.createHorizontalGlue());
	  add(Box.createVerticalGlue());
	  add(buttonPanel, BorderLayout.PAGE_END);

	  // Admin for the window
	  setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  // Exit when close button clicked
	  setTitle(FRAME_TITLE); // "this" JFrame sets title
	  pack();
	  setResizable(false); // So they can't mess around with it
	  setLocationRelativeTo(null); // Center the GUI
	  setVisible(true);   // show it
   }

   /**
	 * The actual nitty gritty of UI creation.
	 * Reminded me of why I hate Java...
	 */
   public void createDataPanel() {
	  program = new JComboBox<String>(programIDs);
	  // SpinnerNumberModel yearModel = new SpinnerNumberModel(1990, 1970, 2019, 1);
	  Calendar cal = Calendar.getInstance ();
	  SpinnerDateModel yearModel = new SpinnerDateModel (cal.getTime(), null, null, Calendar.YEAR);
	  cuttoffYear = new JSpinner(yearModel);
	  dumpKeywords = new JCheckBox ();
	  dumpKeywords.addItemListener (new ItemListener () {
	  	@Override
	  	public void itemStateChanged(ItemEvent e) {
	  		if (e.getStateChange() == ItemEvent.SELECTED) {
	  			dumpingKeywordsBool = true;
	  			// System.out.println ("The check box is checked");
	  		}
	  		else {
	  			dumpingKeywordsBool = false;
	  			// System.out.println ("The check box is unchecked");
	  		}
	  	}
	  });

	  JPanel sideBySidePanel = createSideBySidePanel(new JLabel("Experiment:"), program);
	  textPanel.add(sideBySidePanel);

	  sideBySidePanel = createSideBySidePanel(new JLabel("Dump keywords:"), dumpKeywords);
	  textPanel.add(sideBySidePanel);

	  sideBySidePanel = createSideBySidePanel(new JLabel("Cutoff Year:"), cuttoffYear);
	  textPanel.add(sideBySidePanel);

	  sideBySidePanel = createInputPanelWithChooserButton(new JLabel("Input file:"));
	  textPanel.add(sideBySidePanel);

	  sideBySidePanel = createOutputPanelWithChooserButton(new JLabel("Output directory:"));
	  textPanel.add(sideBySidePanel);
   }

   /**
	 * Factory method for generating box layout panels
	 */
   public JPanel createSideBySidePanel(JLabel label, JComponent ui) {
		JPanel sideBySidePanel = new JPanel();
		sideBySidePanel.setLayout(new BoxLayout(sideBySidePanel, BoxLayout.LINE_AXIS));
		sideBySidePanel.add(Box.createHorizontalGlue());
		sideBySidePanel.add(label);
		sideBySidePanel.add(Box.createHorizontalGlue());
		sideBySidePanel.add(ui);
		sideBySidePanel.add(Box.createHorizontalGlue());
		return sideBySidePanel;
   }

	public JPanel createInputPanelWithChooserButton (JLabel label) {
		JPanel inputPanel = new JPanel ();
		// inputPanel.setPreferredSize(new Dimension(TEXT_PANEL_WIDTH, 40));
		JButton chooserButton = new JButton ("Choose");
		// inputFileTextField = new JTextField ("Input file location:...");
		inputPanel.setLayout(new BoxLayout(inputPanel, BoxLayout.LINE_AXIS));
		inputPanel.add(Box.createHorizontalGlue());
		inputPanel.add(label);
		// inputPanel.add(Box.createHorizontalGlue());
		inputPanel.add(inputFileTextField);
		inputPanel.add(Box.createHorizontalGlue());

  		chooserButton.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent ev) {
				JFileChooser chooser = new JFileChooser();
				FileNameExtensionFilter filter = new FileNameExtensionFilter(
					"bibtex and csv files", "bib", "csv");
				chooser.setFileFilter(filter);
				int returnVal = chooser.showOpenDialog(inputPanel);
				if(returnVal == JFileChooser.APPROVE_OPTION) {
					// System.out.println("You chose to open this file: " +
					//     chooser.getSelectedFile().getName());
					inputFileTextField.setText (chooser.getSelectedFile().getAbsolutePath());
				}
			}

		}); 
		inputPanel.add(chooserButton);
		// inputPanel.add(Box.createHorizontalGlue());

		return inputPanel;
	}

	public JPanel createOutputPanelWithChooserButton (JLabel label) {
		JPanel inputPanel = new JPanel ();
		// inputPanel.setPreferredSize(new Dimension(TEXT_PANEL_WIDTH, 40));
		JButton chooserButton = new JButton ("Choose");
		// inputFileTextField = new JTextField ("Input file location:...");
		inputPanel.setLayout(new BoxLayout(inputPanel, BoxLayout.LINE_AXIS));
		inputPanel.add(Box.createHorizontalGlue());
		inputPanel.add(label);
		// inputPanel.add(Box.createHorizontalGlue());
		inputPanel.add(outputDirectoryTextField);
		inputPanel.add(Box.createHorizontalGlue());

  		chooserButton.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent ev) {
				JFileChooser chooser = new JFileChooser();
				chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
				// FileNameExtensionFilter filter = new FileNameExtensionFilter(
				// 	"bibtex and csv files", "bib", "csv");
				// chooser.setFileFilter(filter);
				int returnVal = chooser.showOpenDialog(inputPanel);
				if(returnVal == JFileChooser.APPROVE_OPTION) {
					// System.out.println("You chose to open this file: " +
					//     chooser.getSelectedFile().getName());
					outputDirectoryTextField.setText (chooser.getSelectedFile().getAbsolutePath());
				}
			}

		});
		inputPanel.add(chooserButton);
		// inputPanel.add(Box.createHorizontalGlue());

		return inputPanel;
	}
 
	/** The entry main() method */
	public static void main(String[] args) {
		// Run GUI codes in the Event-Dispatching thread for thread safety
		SwingUtilities.invokeLater(new Runnable() {
		 public void run() {
			new Main();  // Let the constructor do the job
		 }
		});
	}
}

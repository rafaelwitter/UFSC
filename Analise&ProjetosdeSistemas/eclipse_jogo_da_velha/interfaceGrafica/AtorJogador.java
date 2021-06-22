package interfaceGrafica;

import javax.swing.JPanel;
import java.awt.GraphicsConfiguration;
import java.awt.HeadlessException;

import javax.swing.JFrame;

import dominioProblema.ImagemDeTabuleiro;
import dominioProblema.Tabuleiro;
import javax.swing.JLabel;
import java.awt.Rectangle;

import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;

public class AtorJogador extends JFrame {

	private static final long serialVersionUID = 1L;

	private JPanel jContentPane = null;
	
	protected Tabuleiro tab;  //  @jve:decl-index=0:
	protected String idJ1;
	
	private JLabel vPosicao11 = null;
	private JLabel vPosicao12 = null;
	private JLabel vPosicao13 = null;
	private JLabel vPosicao21 = null;
	private JLabel vPosicao22 = null;
	private JLabel vPosicao23 = null;
	private JLabel vPosicao31 = null;
	private JLabel vPosicao32 = null;
	private JLabel vPosicao33 = null;
	
	protected JLabel mapaVPosicao[][] = new JLabel[3][3];

    private JMenuBar jMenuBar1 = null;
	
	private JMenu menuJogo = null;

	private JMenuItem jMenuItem1 = null;

	private JMenuItem jMenuItem2 = null;

	private JLabel vMensagem = null;


	public AtorJogador() throws HeadlessException {
		// TODO Auto-generated constructor stub
		super();
		initialize();
	}

	public AtorJogador(GraphicsConfiguration arg0) {
		super(arg0);
		// TODO Auto-generated constructor stub
		initialize();
	}

	public AtorJogador(String arg0) throws HeadlessException {
		super(arg0);
		// TODO Auto-generated constructor stub
		initialize();
	}

	public AtorJogador(String arg0, GraphicsConfiguration arg1) {
		super(arg0, arg1);
		// TODO Auto-generated constructor stub
		initialize();
	}

	/**
	 * This method initializes this
	 * 
	 * @return void
	 */
	private void initialize() {
		this.setSize(260, 330);
		this.setContentPane(getJContentPane());
		this.setTitle("Jogo da Velha");
		tab = new Tabuleiro();
		tab.iniciar();
	}

	/**
	 * This method initializes jContentPane
	 * 
	 * @return javax.swing.JPanel
	 */
	private JPanel getJContentPane() {
		if (jContentPane == null) {
			
			Icon vazia = new ImageIcon(getClass().getResource("vazia.gif"));
	//		Icon xis = new ImageIcon(getClass().getResource("xis.gif"));
	//		Icon bola = new ImageIcon(getClass().getResource("bola.gif"));

			vMensagem = new JLabel();
			vMensagem.setBounds(new Rectangle(25, 10, 200, 20));
			vMensagem.setText("www.inf.ufsc.br/ricardo");
			
			vPosicao11 = new JLabel();
			vPosicao11.setBounds(new Rectangle(20, 40, 70, 70));
			vPosicao11.setIcon(vazia);				
			vPosicao11.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					click(1,1); 
				}
			});
			vPosicao12 = new JLabel();
			vPosicao12.setBounds(new Rectangle(90, 40, 70, 70));
			vPosicao12.setIcon(vazia);
			vPosicao12.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					click(1,2); 
				}
			});
			vPosicao13 = new JLabel();
			vPosicao13.setIcon(vazia);
			vPosicao13.setBounds(new Rectangle(160, 40, 70, 70));
			vPosicao13.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					click(1,3); 
				}
			});
			vPosicao21 = new JLabel();
			vPosicao21.setBounds(new Rectangle(20, 110, 70, 70));
			vPosicao21.setIcon(vazia);
			vPosicao21.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					click(2,1); 
				}
			});
			vPosicao22 = new JLabel();
			vPosicao22.setBounds(new Rectangle(90, 110, 70, 70));
			vPosicao22.setIcon(vazia);
			vPosicao22.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					click(2,2); 
				}
			});
			vPosicao23 = new JLabel();
			vPosicao23.setBounds(new Rectangle(160, 110, 70, 70));
			vPosicao23.setIcon(vazia);
			vPosicao23.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					click(2,3); 
				}
			});
			vPosicao31 = new JLabel();
			vPosicao31.setBounds(new Rectangle(20, 180, 70, 70));
			vPosicao31.setIcon(vazia);
			vPosicao31.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					click(3,1); // TODO Auto-generated Event stub mouseClicked()
				}
			});
			vPosicao32 = new JLabel();
			vPosicao32.setBounds(new Rectangle(90, 180, 70, 70));
			vPosicao32.setIcon(vazia);
			vPosicao32.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					click(3,2); 
				}
			});
			vPosicao33 = new JLabel();
			vPosicao33.setBounds(new Rectangle(160, 180, 70, 70));
			vPosicao33.setIcon(vazia);
			vPosicao33.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					click(3,3); 
				}
			});
			jMenuBar1 = new JMenuBar();
			jMenuBar1.add(getMenu());
		    this.setJMenuBar(jMenuBar1);

			jContentPane = new JPanel();
			jContentPane.setLayout(null);
			jContentPane.add(vPosicao11, null);
			jContentPane.add(vPosicao12, null);
			jContentPane.add(vPosicao13, null);
			jContentPane.add(vPosicao21, null);
			jContentPane.add(vPosicao22, null);
			jContentPane.add(vPosicao23, null);
			jContentPane.add(vPosicao31, null);
			jContentPane.add(vPosicao32, null);
			jContentPane.add(vPosicao33, null);
			
			mapaVPosicao[0][0] = vPosicao11;
			mapaVPosicao[0][1] = vPosicao12;
			mapaVPosicao[0][2] = vPosicao13;			
			mapaVPosicao[1][0] = vPosicao21;
			mapaVPosicao[1][1] = vPosicao22;
			mapaVPosicao[1][2] = vPosicao23;
			mapaVPosicao[2][0] = vPosicao31;
			mapaVPosicao[2][1] = vPosicao32;
			mapaVPosicao[2][2] = vPosicao33;

			jContentPane.add(vMensagem, null);
		}
		return jContentPane;
	}
	 
	public void iniciarPartida() {
		boolean emAndamento = false;
		boolean autoriza = true;
		boolean contraPrograma = true;
		boolean simbolo = true;		
		String idJ2 = "programa";
		
		if (tab == null){
			tab = new Tabuleiro();
			tab.iniciar();
		};
		emAndamento = tab.InformarPartidaEmAndamento();
		if (emAndamento) {
			autoriza = this.avaliarInterrupcao();			
		};
		if (!emAndamento || autoriza){
			contraPrograma = this.avaliarContraPrograma();
			idJ1 = this.obterIdJogador(" 1");
			simbolo = this.obterSimboloJogador();
			tab.criarJogadorHumano(idJ1, simbolo);
			if (contraPrograma) {
				tab.criarJogadorAutomatico(idJ2, !simbolo);		
			}
			else {
				idJ2 = this.obterIdJogador(" 2");
				tab.criarJogadorHumano(idJ2, !simbolo);	
			};
			this.estabelecerSequenciamento();				
		};
	}
	 
	public boolean avaliarInterrupcao() {
		boolean afirmativo = false;
		boolean condRepetir = true;
		int resposta;
		while (condRepetir) {
			resposta = JOptionPane.showConfirmDialog(this, "Deseja interromper partida em andamento?");
			afirmativo = resposta == JOptionPane.YES_OPTION;
			condRepetir = resposta == JOptionPane.CANCEL_OPTION;
		};
		return afirmativo;
}

	public boolean avaliarContraPrograma() {
		boolean afirmativo = false;
		boolean condRepetir = true;
		int resposta;
		while (condRepetir) {
			resposta = JOptionPane.showConfirmDialog(this, "Deseja jogar contra o programa?");
			afirmativo = resposta == JOptionPane.YES_OPTION;
			condRepetir = resposta == JOptionPane.CANCEL_OPTION;
		};
		return afirmativo;
}
 
	public String obterIdJogador(String ordem) {
		String idJogador = ("jogador" + ordem);
		idJogador = JOptionPane.showInputDialog(this, ("Insira o nome do jogador" + ordem));
		return idJogador;
	}
	 
	public void estabelecerSequenciamento() {
		this.definirOPrimeiro();
		this.exibirEstado();
	}
	 
	public void definirOPrimeiro() {
		boolean afirmativo = false;
		boolean condRepetir = true;
		int resposta;
		while (condRepetir) {
			resposta = JOptionPane.showConfirmDialog(this, (idJ1 + " inicia a partida?"));
			afirmativo = resposta == JOptionPane.YES_OPTION;
			condRepetir = resposta == JOptionPane.CANCEL_OPTION;
		};
		if (afirmativo) {
			tab.definirOPrimeiro(1);
		} else {
			tab.definirOPrimeiro(2);
		};
	}
	 
	public boolean obterSimboloJogador() {
	       return (DialogoSimbolo.informaSimbolo("Qual o simbolo do jogador " + idJ1 + "?"));
//		return false;
	}
	 
	public void reiniciarPartida() {
		boolean emAndamento = false;
		boolean autoriza = false;
		boolean jogadores = false;
		if (tab == null){
			this.iniciarPartida();
		} else {		// ;
			emAndamento = tab.InformarPartidaEmAndamento();
			jogadores = tab.informarExistenciaJogadores();
			if (jogadores) {
				if (emAndamento) {
					autoriza = this.avaliarInterrupcao();
				};	
				if (!emAndamento || autoriza){
						this.estabelecerSequenciamento();				
				};
			}else {
				this.iniciarPartida();
				};
		};
	}
	 
	public void click(int linha, int coluna) {
		int resultado = 0;
		resultado = tab.click(linha, coluna);
		if (resultado == 0){
			this.exibirEstado();
		}else {
			this.notificarIrregularidade(resultado);		
		};
	}
	 
	public void exibirEstado() {
		ImagemDeTabuleiro estado;
		int valor = 0;
		Icon vazia = new ImageIcon(getClass().getResource("vazia.gif"));
		Icon xis = new ImageIcon(getClass().getResource("xis.gif"));
		Icon bola = new ImageIcon(getClass().getResource("bola.gif"));
		estado = tab.informarEstado();
		vMensagem.setText(estado.informarMensagem());
		for (int linha=1; linha<4; linha++){
			for (int coluna=1; coluna<4; coluna++){
				valor = estado.informarValor(linha, coluna);
				switch (valor){
				case 0: mapaVPosicao[(linha-1)][(coluna-1)].setIcon(vazia);
				break;
				case 1: mapaVPosicao[(linha-1)][(coluna-1)].setIcon(xis);
				break;
				case 2: mapaVPosicao[(linha-1)][(coluna-1)].setIcon(bola);
				}
			};
		};
		}
	 
	public void notificarIrregularidade(int codigo) {
		if (codigo == 2){
			JOptionPane.showMessageDialog(this, "Partida encerrada ou não iniciada");
		}else {
			JOptionPane.showMessageDialog(this, "Posição ocupada. Jogue novamente");	
		};
	}

	/**
	 * This method initializes Jogo	
	 * 	
	 * @return javax.swing.JMenu	
	 */
	private JMenu getMenu() {
		if (menuJogo == null) {
			menuJogo = new JMenu();
			menuJogo.setText("Jogo");
			menuJogo.setBounds(new Rectangle(1, 0, 57, 21));
			menuJogo.add(getJMenuItem1());
			menuJogo.add(getJMenuItem2());
		}
		return menuJogo;
	}

	/**
	 * This method initializes jMenuItem1	
	 * 	
	 * @return javax.swing.JMenuItem	
	 */
	private JMenuItem getJMenuItem1() {
		if (jMenuItem1 == null) {
			jMenuItem1 = new JMenuItem();
			jMenuItem1.setText("iniciar nova partida");
			jMenuItem1.addActionListener(new java.awt.event.ActionListener() {
				public void actionPerformed(java.awt.event.ActionEvent e) {
					iniciarPartida();
				}
			});
		}
		return jMenuItem1;
	}

	/**
	 * This method initializes jMenuItem2	
	 * 	
	 * @return javax.swing.JMenuItem	
	 */
	private JMenuItem getJMenuItem2() {
		if (jMenuItem2 == null) {
			jMenuItem2 = new JMenuItem();
			jMenuItem2.setText("reiniciar partida");
			jMenuItem2.addActionListener(new java.awt.event.ActionListener() {
				public void actionPerformed(java.awt.event.ActionEvent e) {
					reiniciarPartida();
				}
			});
		}
		return jMenuItem2;
	}

}

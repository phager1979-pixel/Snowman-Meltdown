STAGES = [
    # Stage 0: Vollständiger Schneemann
    """
      ___
     /___\\
    / O 0 \\
    | <=> |
   __\---/__
  /    o     \\
 /     o      \\
 \\     o      /
  \\----------/
 /--        --\\
/______________\\
    """,

    # Stage 1: Unterste 2 Zeilen verschwinden
    """
      ___
     /___\\
    / O 0 \\
    | <=> |
   __\---/__
  /    o     \\
 /     o      \\
 \\     o      /
  \\----------/
    """,

    # Stage 2: Weitere 2 untere Zeilen verschwinden
    """
      ___
     /___\\
    / O 0 \\
    | <=> |
   __\---/__
  /    o     \\
 /     o      \\
    """,

    # Stage 3: Weitere 2 untere Zeilen verschwinden
    """
      ___
     /___\\
    / O 0 \\
    | <=> |
   __\---/__
    """,

    # Stage 4: Nur der Kopf bleibt
    """
      ___
     /___\\
    / X X \\
    """
]

VICTORY = [
    # WIN-Stage 0: Rakete steigt auf
    """
              .
              .
              .
              |
              |
              |
              |
    """,
    # WIN-Stage 1: Erste kleine Explosion
    """
             \\|/
            --*--
             /|\\
    """,
    # WIN-Stage 2: Groessere Explosion
    """
           \\  |  /
         '  \\ | /  '
          -- * | * --
          '  / | \\  '
            /  |  \\
    """,
    # WIN-Stage 3: Mehrere Explosionen gleichzeitig
    """
         \\    |    /
     *    \\   |   /    *
   .   '.  \\  |  /  .'   .
 '   *    ' \\ | / '    *   '
 - - - - - - \\|/ - - - - - -
     .   ,'  /|\\  ',   .
   '     ,' / | \\ ',     '
    *      /  |  \\      *
          /   |   \\
    """,
    # WIN-Stage 4: Finale - volles Feuerwerk mit VICTORY-Schriftzug
    """
         \\    |    /
     *    \\   |   /    *
   .   '.  \\  |  /  .'   .
 '   *    ' \\ | / '    *   '
 - - - - - - \\|/ - - - - - -
     .   ,'  /|\\  ',   .
   '     ,' / | \\ ',     '
    *      /  |  \\      *
          /   |   \\

 *  *  *   VICTORY!   *  *  *
    """
]
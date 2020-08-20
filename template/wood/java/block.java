	//%BLOCK_UPPER% TREE

	public static final RegistryObject<Block> %BLOCK_UPPER%_LOG = BLOCKS.register("%BLOCK%_log",
			() -> new LogBlock(MaterialColor.WOOD, Block.Properties.from(Blocks.DARK_OAK_LOG)));
	
	public static final RegistryObject<Block> %BLOCK_UPPER%_PLANKS = BLOCKS.register("%BLOCK%_planks",
			() -> new Block(Block.Properties.from(Blocks.DARK_OAK_PLANKS)));

	public static final RegistryObject<Block> %BLOCK_UPPER%_STAIRS = BLOCKS.register("%BLOCK%_stairs",
			() -> new StairsBlock(() -> BlockInit.%BLOCK_UPPER%_PLANKS.get().getDefaultState(),
					Block.Properties.create(Material.WOOD, MaterialColor.WOOD)));

	public static final RegistryObject<Block> %BLOCK_UPPER%_FENCE = BLOCKS.register("%BLOCK%_fence",
			() -> new FenceBlock(Block.Properties.create(Material.WOOD, MaterialColor.WOOD)));
	
	public static final RegistryObject<Block> %BLOCK_UPPER%_FENCE_GATE = BLOCKS.register("%BLOCK%_fence_gate",
			() -> new FenceGateBlock(Block.Properties.create(Material.WOOD, MaterialColor.WOOD)));

	public static final RegistryObject<Block> %BLOCK_UPPER%_BUTTON = BLOCKS.register("%BLOCK%_button",
			() -> new %JAVA_CLASS%WoodButtonBlock(Block.Properties.create(Material.WOOD, MaterialColor.WOOD)));
	
	public static final RegistryObject<Block> %BLOCK_UPPER%_PRESSURE_PLATE = BLOCKS.register("%BLOCK%_pressure_plate",
			() -> new %JAVA_CLASS%PressurePlateBlock(Sensitivity.EVERYTHING,
					Block.Properties.create(Material.WOOD, MaterialColor.WOOD)));
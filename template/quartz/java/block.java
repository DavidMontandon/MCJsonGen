	//%BLOCK_UPPER%
	
	public static final RegistryObject<Block> %BLOCK_UPPER%_BLOCK = BLOCKS.register("%BLOCK%_block",
			() -> new Block(Block.Properties.create(Material.ROCK, MaterialColor.QUARTZ).hardnessAndResistance(0.8F)));

	public static final RegistryObject<Block> CHISELED_%BLOCK_UPPER%_BLOCK = BLOCKS.register("chiseled_%BLOCK%_block",
			() -> new Block(Block.Properties.create(Material.ROCK, MaterialColor.QUARTZ).hardnessAndResistance(0.8F)));

	public static final RegistryObject<Block> %BLOCK_UPPER%_PILLAR = BLOCKS.register("%BLOCK%_pillar",
			() -> new RotatedPillarBlock(Block.Properties.create(Material.ROCK, MaterialColor.QUARTZ).hardnessAndResistance(0.8F)));

	public static final RegistryObject<Block> %BLOCK_UPPER%_STAIRS = BLOCKS.register("%BLOCK%_stairs",
			() -> new StairsBlock(() -> BlockInit.%BLOCK_UPPER%_BLOCK.get().getDefaultState(),
					Block.Properties.create(Material.ROCK, MaterialColor.QUARTZ)));
	
	public static final RegistryObject<Block> SMOOTH_%BLOCK_UPPER% = BLOCKS.register("smooth_%BLOCK%",
			() -> new Block(Block.Properties.create(Material.ROCK, MaterialColor.QUARTZ).hardnessAndResistance(0.8F)));

	public static final RegistryObject<Block> SMOOTH_%BLOCK_UPPER%_STAIRS = BLOCKS.register("smooth_%BLOCK%_stairs",
			() -> new StairsBlock(() -> BlockInit.SMOOTH_%BLOCK_UPPER%.get().getDefaultState(),
					Block.Properties.create(Material.ROCK, MaterialColor.QUARTZ)));
					
	public static final RegistryObject<Block> %BLOCK_UPPER%_SLAB = BLOCKS.register("%BLOCK%_slab",
			() -> new SlabBlock(Block.Properties.create(Material.ROCK, MaterialColor.QUARTZ).hardnessAndResistance(2.0F, 6.0F)));

	public static final RegistryObject<Block> SMOOTH_%BLOCK_UPPER%_SLAB = BLOCKS.register("smooth_%BLOCK%_slab",
			() -> new SlabBlock(Block.Properties.create(Material.ROCK, MaterialColor.QUARTZ).hardnessAndResistance(2.0F, 6.0F)));
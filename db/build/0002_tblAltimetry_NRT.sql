USE [Opedia]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblAltimetry_NRT](
	[lat] [float] NOT NULL,
	[lon] [float] NOT NULL,
	[time] [date] NOT NULL,
	[vgosa_nrt] [float] NULL,
	[vgos_nrt] [float] NULL,
	[sla_nrt] [float] NULL,
	[adt_nrt] [float] NULL,
	[ugosa_nrt] [float] NULL,
	[ugos_nrt] [float] NULL,
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_tblAltimetry_NRT] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [FG2]
) ON [FG2]

GO




---------------------
-- Indices
---------------------

-- No index is defined on the velocity fields. This may change in future, if needed.


CREATE UNIQUE NONCLUSTERED INDEX [IX_tblAltimetry_NRT_time_lat_lon] ON [dbo].[tblAltimetry_NRT]
(
	[time] ASC,
	[lat] ASC,
	[lon] ASC
)
INCLUDE ([sla_nrt], [adt_nrt]) 
WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
ON [FG2]
GO

/*
CREATE NONCLUSTERED INDEX [IX_tblAltimetry_NRT_sla] ON [dbo].[tblAltimetry_NRT]
(
	[sla_nrt] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG2]
GO


CREATE NONCLUSTERED INDEX [IX_tblAltimetry_NRT_adt] ON [dbo].[tblAltimetry_NRT]
(
	[adt_nrt] ASC
)WITH (DATA_COMPRESSION = PAGE, PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) 
ON [FG2]
GO
*/


#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# version 1.0.0
#
# GimpPythonFuLayerAction-2-8.py
# Copyright (C) 2012 かんら・から http://www.pixiv.net/member.php?id=3098715
# 
# GimpPythonFuLayerAction-2-8.py is Python-fu plugin for GIMP 2.8
#
# GimpPythonFuLayerAction-2-8.py is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#  
# GimpPythonFuLayerAction-2-8.py is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# GPLv3 ライセンス
# かんら・から http://www.pixiv.net/member.php?id=3098715
# バグレポート・アイデアなどは pixiv メッセージでお願いします。
#
# ダウンロード
# http://www.magic-object.mydns.jp/
#
# このスクリプトを使用して発生した問題に関し、作成者は如何なる保証などを行う事はありません。
# 自己責任でのみの使用を許可します。
########################################################################
from gimpfu import *
########################################################################
########################################################################
# レイヤー操作クラス
#
# レイヤー転写機能群など
#
class LayserActions:
	########################################################################
	image = None
	doPutMessage = True
	lastMessage = ''
	usableVersion = ( 2, 8, 0 )
	canUseLayerGroup = False
	########################################################################
	def __init__( self, image ):
		self.image = image
		versionLength = len( self.usableVersion )
		for index in range( 0, versionLength ) :
			if self.usableVersion[index] < gimp.version[index] :
				self.canUseLayerGroup = True
				break
			elif self.usableVersion[index] == gimp.version[index] :
				if index == ( versionLength - 1 ) :
					self.canUseLayerGroup = True
					break
				continue
			else :
				self.canUseLayerGroup = False
				break
		return
	########################################################################
	# エラーメッセージ機能
	#
	def errorMessage( self, message=None ) :
		if self.doPutMessage :
			if message is None :
				message = self.lastMessage
			else :
				self.lastMessage = message
			
# 			print message
			pdb.gimp_message_set_handler( MESSAGE_BOX )
			pdb.gimp_message( message )
			# MESSAGE_BOX CONSOLE ERROR_CONSOLE
			#gimp.message( message )
		return
	########################################################################
	# 対象レイヤーがイメージの中にあるかどうか？
	#
	def isInImage( self, targetLayer=None, parent=None ) :
		##############################################################
		if targetLayer is None :
			return False
		##############################################################
		if parent is None :
			if targetLayer in self.image.layers :
				return True
			elif not self.canUseLayerGroup :
				return False

			for item in self.image.layers :
				if pdb.gimp_item_is_group( item ) :
					if self.isInImage( targetLayer, item ) :
						return True
		##############################################################
		elif self.canUseLayerGroup :
			( num_children, child_ids ) = pdb.gimp_item_get_children( parent )
			if num_children < 1 :
				return False
			for itemId in child_ids :
				item = gimp.Item.from_id( itemId )
				if pdb.gimp_item_is_group( item ) :
					if self.isInImage( targetLayer, item ) :
						return True
					else :
						continue
				elif item == targetLayer :
					return True
		##############################################################
		return False
	########################################################################
	# 対象がレイヤーグループかどうか？
	#
	def isLayerGroup( self, target=None ) :
		if target is None :
			return False
		elif not self.canUseLayerGroup :
			return False
		else :
			return pdb.gimp_item_is_group( target )
	########################################################################
	# 対象が通常レイヤーかどうか？
	#
	def isNormalLayer( self, target=None ) :
		if target is None :
			return False
		elif self.isLayerGroup( target ) :
			return False
		elif pdb.gimp_item_is_text_layer( target ) :
			return False
		else :
			return pdb.gimp_item_is_layer( target )
	########################################################################
	# レイヤーを拾い上げる
	#
	def pickUpLayersLayer( self,
		targetLayer=None,
		searchRecursive=True,
		needCheckVisible=True,
		searchLayerGroupNumMax=1,
		searchLayerNumMax=100,
		parent=None
		 ) :
		##############################################################
		if targetLayer is None :
			return []
		##############################################################
		pickUppedList = []
		##############################################################
		if parent is None :
			# 直接呼び出し
			##############################################################
			belongLayers = self.image.layers
			##############################################################
			if targetLayer not in belongLayers :
				# 対象レイヤーがトップレベルに無い
				parent = pdb.gimp_item_get_parent( targetLayer )
				if parent is None :
					return []
				else :
					# 対象がレイヤーグループ内に存在
					( num_children, child_ids ) = pdb.gimp_item_get_children( parent )
					if num_children < 1 :
						return []
					for itemId in child_ids :
						belongLayers.append( gimp.Item.from_id( itemId ) )
			if len( belongLayers ) < 1 :
				return []
			##############################################################
			targetIndex = -1
			try :
				targetIndex = belongLayers.index( targetLayer )
			except :
				self.lastMessage = '不適切なレイヤーが指定されています。'
				return []
			##############################################################
			for layer in belongLayers[ targetIndex + 1 : ] :
				if searchLayerNumMax < 1 and searchLayerGroupNumMax < 1 :
					return pickUppedList
				elif needCheckVisible and not pdb.gimp_item_get_visible( layer ) :
					continue
				elif self.isLayerGroup( layer ) :
					##############################################
					if searchLayerGroupNumMax < 1 :
						continue
					##############################################
					searchLayerGroupNumMax -= 1
					resultsLayer = self.pickUpLayersLayer( 
						targetLayer,
						searchRecursive,
						needCheckVisible,
						searchLayerGroupNumMax,
						searchLayerNumMax,
						layer
						)
					pickUppedList += resultsLayer
				elif self.isNormalLayer( layer ) :
					##############################################
					if searchLayerNumMax < 1 :
						continue
					##############################################
					searchLayerNumMax -= 1
					pickUppedList.append( layer )
			##############################################################
			return pickUppedList
		##############################################################
		elif self.canUseLayerGroup :
			# 再帰呼び出し
			##############################################################
			( num_children, child_ids ) = pdb.gimp_item_get_children( parent )
			if num_children < 1 :
				return []
			for itemId in child_ids :
				##############################################################
				item = gimp.Item.from_id( itemId )
				if needCheckVisible and not pdb.gimp_item_get_visible( item ) :
					continue
				elif self.isLayerGroup( item ) :
					if not searchRecursive :
						continue 
					resultsLayer = self.pickUpLayersLayer( 
						targetLayer,
						searchRecursive,
						needCheckVisible,
						searchLayerGroupNumMax,
						searchLayerNumMax,
						item
						)
					pickUppedList += resultsLayer
				elif self.isNormalLayer( item ) :
					pickUppedList.append( item )
			##############################################################
			return pickUppedList
		##############################################################
		return pickUppedList
	########################################################################
	# レイヤーを検索する
	#
	def searchLayer( self,
		targetLayer=None,
		searchRecursive=True,
		needCheckVisible=True,
		searchLayerGroupNumMax=1,
		searchLayerNumMax=0
		 ) :
		##############################################################
		if targetLayer is None :
			if self.image is None :
				self.lastMessage = 'パラメータが不正です。'
				return []
			targetLayer = self.image.active_layer
		##############################################################
		if targetLayer is None :
			self.lastMessage = 'レイヤーが選択されていません。'
			return []
		elif not self.isInImage( targetLayer ) :
			self.lastMessage = '不適切なレイヤーが指定されています。'
			return []
		elif not self.isNormalLayer( targetLayer ) :
			self.lastMessage = '対象がレイヤーではありません。'
			return []
		elif self.isLayerGroup( targetLayer ) :
			self.lastMessage = 'レイヤーグループを対象にする事はできません。'
			return []
		elif searchLayerGroupNumMax < 1 and searchLayerNumMax < 1 :
			self.lastMessage = '制限数が設定されていません。'
			return []
		##############################################################
		pickUppedList = self.pickUpLayersLayer(
			targetLayer,
			searchRecursive,
			needCheckVisible,
			searchLayerGroupNumMax,
			searchLayerNumMax,
			None
		 	)
		if len( pickUppedList ) < 1 :
			self.lastMessage = '対象が見つかりませんでした。'
			return pickUppedList
		##############################################################
		return pickUppedList
		
	########################################################################
	# ターゲットのレイヤーに対し転写が可能かどうかチェックする
	#
	def canDoTranscribe( self, targetLayer=None ) :
		##############################################################
		if targetLayer is None :
			if self.image is None :
				self.lastMessage = 'パラメータが不正です。'
				return False
			targetLayer = self.image.active_layer
		##############################################################
		if targetLayer is None :
			self.lastMessage = 'レイヤーが選択されていません。'
			return False
		elif not self.isInImage( targetLayer ) :
			self.lastMessage = '不適切なレイヤーが指定されています。'
			return False
		elif not self.isNormalLayer( targetLayer ) :
			self.lastMessage = '対象がレイヤーではありません。'
			return False
		elif self.isLayerGroup( targetLayer ) :
			self.lastMessage = 'レイヤーグループに対して転写を行う事は出来ません。'
			return False
		##############################################################
		# 対象レイヤーを含む、連続する通常レイヤーのリストを作成
		layerList = []
		parent = pdb.gimp_item_get_parent( targetLayer )

		if parent is None :
			for item in self.image.layers :
				if self.isNormalLayer( item ) :
					if targetLayer in layerList :
						return True
					else :
						layerList.append( item )
				else :
					layerList = []
					continue
		else :
			( num_children, child_ids ) = pdb.gimp_item_get_children( parent )
			for itemId in child_ids :
				item = gimp.Item.from_id( itemId )
				if self.isNormalLayer( item ) :
					if targetLayer in layerList :
						return True
					else :
						layerList.append( item )
				else :
					layerList = []
					continue
		##############################################################
		# 問題が無ければ通常、ここまで来ない
		# エラー解析
		if len( layerList ) < 2 :
			self.lastMessage = '転写を行うには、転写元と転写先のレイヤーが必要です。'
			return False
		elif targetLayer not in layerList :
			self.lastMessage = '下位に適切なレイヤーがありません。'
			return False
		else :
			targetIndex = -1
			try :
				targetIndex = layerList.index( targetLayer )
			except :
				self.lastMessage = '不適切なレイヤーが指定されています。'
				return False
			if targetIndex == ( len( layerList ) - 1 ) :
				self.lastMessage = '下位に適切なレイヤーがありません。'
				return False
		##############################################################
		self.lastMessage = 'エラーが発生しましたが、解析に失敗しました。'
		return False
	########################################################################
	# 転写を実行する
	#
	def transcribe( self, targetLayer=None ) :
		##############################################################
		# 対象のレイヤーチェック
		if not self.canDoTranscribe() :
			self.errorMessage()
			return False
		##############################################################
		if targetLayer is None :
			if self.image is None :
				self.lastMessage = 'パラメータが不正です。'
				self.errorMessage()
				return False
			targetLayer = self.image.active_layer
		##############################################################
		if targetLayer is None :
			self.lastMessage = 'レイヤーが選択されていません。'
			self.errorMessage()
			return False
		##############################################################
		# 転写先のレイヤーを取得
		againstLayer = None
		parent = pdb.gimp_item_get_parent( targetLayer )
		if parent is None :
			targetIndex = -1
			try :
				targetIndex = self.image.layers.index( targetLayer )
			except :
				self.lastMessage = '不適切なレイヤーが指定されています。'
				self.errorMessage()
				return False
		
			againstLayer = self.image.layers[ targetIndex + 1 ]
		else :
			layerList = []
			( num_children, child_ids ) = pdb.gimp_item_get_children( parent )
			for itemId in child_ids :
				item = gimp.Item.from_id( itemId )
				if self.isNormalLayer( item ) :
					if targetLayer in layerList :
						againstLayer = item
						break
					else :
						layerList.append( item )
		if againstLayer is None :
			self.lastMessage = '転写先のレイヤーを取得出来ませんでした。'
			self.errorMessage()
			return False
		##############################################################
		# 転写元のレイヤーを作成しておく
		# データなしの複製
		newLayer = gimp.Layer(
			self.image,
			targetLayer.name,
			targetLayer.width,
			targetLayer.height,
			targetLayer.type,
			targetLayer.opacity,
			targetLayer.mode
			)
		# レイヤーマスクを設定
		if targetLayer.mask is not None :
			pdb.gimp_image_add_layer_mask( self.image, newLayer, targetLayer.mask.copy() )
		# 透明部分を保護
		# pdb.gimp_layer_set_lock_alpha( newLayer, pdb.gimp_layer_get_lock_alpha( targetLayer ) )
		##############################################################
		# 転写先のレイヤーマスクを複製
		againstLayerMask = None
		if againstLayer.mask is not None :
			againstLayerMask = againstLayer.mask.copy()
		##############################################################
		# 転写先のレイヤーモードを保持
		againstLayerMode = againstLayer.mode
		##############################################################
		# 下のレイヤーと統合
		resultsLayer = pdb.gimp_image_merge_down( self.image, targetLayer, CLIP_TO_BOTTOM_LAYER )
		# レイヤーマスクを設定
		if againstLayerMask is not None :
			pdb.gimp_image_add_layer_mask( self.image, resultsLayer, againstLayerMask )
		# レイヤーモードを設定
		pdb.gimp_layer_set_mode( resultsLayer, againstLayerMode )
		##############################################################
		# 転写元のレイヤーを挿入
		pdb.gimp_image_set_active_layer( self.image, resultsLayer )
		pdb.gimp_image_insert_layer(
			self.image,
			newLayer,
			pdb.gimp_item_get_parent(resultsLayer),
			-1
			)
		##############################################################
		return True
	########################################################################
	# クリップマスク作成する
	#
	def createLayerClip(
		self,
		targetLayer=None,
		searchRecursive=True,
		mergeAlpha=True,
		mergeLayerMask=True,
		needCheckVisible=True,
		mergeClipLayerMask=True,
		searchLayerGroupNumMax=1,
		searchLayerNumMax=0
		) :
		########################################################################
		if targetLayer is None :
			if self.image is None :
				self.lastMessage = 'パラメータが不正です。'
				self.errorMessage()
				return False
			targetLayer = self.image.active_layer
		##############################################################
		if targetLayer is None :
			self.lastMessage = 'レイヤーが選択されていません。'
			self.errorMessage()
			return False
		elif not self.isInImage( targetLayer ) :
			self.lastMessage = '不適切なレイヤーが指定されています。'
			self.errorMessage()
			return False
		elif not self.isNormalLayer( targetLayer ) :
			self.lastMessage = '対象がレイヤーではありません。'
			self.errorMessage()
			return False
		elif self.isLayerGroup( targetLayer ) :
			self.lastMessage = 'レイヤーグループを対象にする事はできません。'
			self.errorMessage()
			return False
		elif searchLayerGroupNumMax < 1 and searchLayerNumMax < 1 :
			self.lastMessage = '制限数が設定されていません。'
			self.errorMessage()
			return False
		elif ( not mergeAlpha ) and ( not mergeLayerMask ) :
			self.lastMessage = 'アルファマスクかレイヤーマスクを指定しなければなりません。'
			self.errorMessage()
			return False
		if not self.canUseLayerGroup and searchLayerNumMax < 1 :
			self.lastMessage = '制限数が設定されていません。'
			self.errorMessage()
			return False
		##############################################################
		pdb.gimp_progress_update(float(0)/float(6))
		##############################################################
		# 対象レイヤーを検索
		resultsLayers = self.searchLayer(
			targetLayer,
			searchRecursive,
			needCheckVisible,
			searchLayerGroupNumMax,
			searchLayerNumMax
			 )
		if len( resultsLayers ) < 1 :
			self.errorMessage()
			return False
		##############################################################
		pdb.gimp_progress_update(float(1)/float(6))
		##############################################################
		# UNDO スタックをフリーズ
		#pdb.gimp_image_undo_freeze( self.image )
		##############################################################
		# 空のマスクを作成
		layersMask = pdb.gimp_layer_create_mask( targetLayer, ADD_BLACK_MASK )
		##############################################################
		pdb.gimp_progress_update(float(2)/float(6))
		##############################################################
		# 検索結果からマスクを作成
		for layer in resultsLayers :
			##############################################################
			# レイヤーが「標準」または「ディザ合成」でない場合はマスクを収集しない
			if pdb.gimp_layer_get_mode( layer ) not in [ NORMAL_MODE, DISSOLVE_MODE ] :
				continue
			##############################################################
			clipMask = None
			alphaMask = None
			if mergeAlpha :
				##############################################################
				# アルファマスクを取得
				alphaMask = pdb.gimp_layer_create_mask( layer, ADD_ALPHA_MASK )
				clipMask = alphaMask
				##############################################################
			if mergeLayerMask and layer.mask is not None:
				##############################################################
				if clipMask is None :
					# レイヤーマスクをクリップマスクに
					clipMask = layer.mask.copy()
				else :
					# アルファマスクとレイヤーマスクの共通部分をクリップマスクに
					pdb.gimp_channel_combine_masks( clipMask, layer.mask, CHANNEL_OP_INTERSECT, 0, 0 )
				##############################################################
			##############################################################
			if clipMask is None :
				continue
			##############################################################
			# クリップマスクを加算
			( layerOffsetX, layerOffsetY ) = pdb.gimp_drawable_offsets( layer )
			( targetOffsetX, targetOffsetY ) = pdb.gimp_drawable_offsets( targetLayer )
			offsetX =  layerOffsetX - targetOffsetX
			offsetY =  layerOffsetY - targetOffsetY
			pdb.gimp_channel_combine_masks( layersMask, clipMask, CHANNEL_OP_ADD, offsetX, offsetY )
			pdb.gimp_item_delete( clipMask )
			clipMask = None
			##############################################################
		##############################################################
		pdb.gimp_progress_update(float(3)/float(6))
		##############################################################
		if mergeClipLayerMask and targetLayer.mask is not None :
			# 対象レイヤーのレイヤーマスクでクリップ
			pdb.gimp_channel_combine_masks( layersMask, targetLayer.mask, CHANNEL_OP_INTERSECT, 0, 0 )
		##############################################################
		pdb.gimp_progress_update(float(4)/float(6))
		##############################################################
		# UNDO スタックをフリーズ解除
		#pdb.gimp_image_undo_thaw( self.image )
		##############################################################
		if targetLayer.mask is not None :
			# もし、対象レイヤーのレイヤーマスクがあれば削除
			pdb.gimp_image_remove_layer_mask( self.image, targetLayer, MASK_APPLY )
		##############################################################
		pdb.gimp_progress_update(float(5)/float(6))
		##############################################################
		# レイヤーマスクにクリップマスクを設定
		pdb.gimp_layer_add_mask( targetLayer, layersMask )
		#pdb.gimp_image_set_active_layer( self.image, targetLayer )
		##############################################################
		pdb.gimp_progress_update(float(6)/float(6))
		##############################################################
		return True
	########################################################################
########################################################################
# レイヤー転写機能
# レイヤーマスク、レイヤーグループ対応
#
def python_fu_tensha_2_8( image, drawable ) :
	
	layerAction = LayserActions( image )

	# 転写を実行
	image.undo_group_start()
	layerAction.transcribe()
	image.undo_group_end()
	return

########################################################################
# クリップマスク作成機能
# 対象となるレイヤーやレイヤーグループから、クリッピングマスクを作成
#
def python_fu_clip_layer(
	image,
	drawable,
	searchRecursive=True,
	mergeAlpha=True,
	mergeLayerMask=True,
	needCheckVisible=True,
	mergeClipLayerMask=True,
	searchLayerGroupNumMax=1,
	searchLayerNumMax=100
	) :
	# ダイアログを出すと
	# (gimp:14434): Gimp-Core-CRITICAL **: gimp_channel_push_undo: assertion `gimp_item_is_attached (GIMP_ITEM (channel))' failed
	# が出る。回避策が無い
	
	layerAction = LayserActions( image )
	
	# クリップマスクを作成
	image.undo_group_start()
	layerAction.createLayerClip(
		None,
		searchRecursive,
		mergeAlpha,
		mergeLayerMask,
		needCheckVisible,
		mergeClipLayerMask,
		searchLayerGroupNumMax,
		searchLayerNumMax
	)
	image.undo_group_end()
	return

########################################################################

register(
	'python-fu-tensha-2-8',			# プロシジャの名前
	'転写スクリプト。アクティブなレイヤーの内容を、下にあるレイヤーに転写する。',
	# プロシジャの説明文
	'ver 2.8 以上を対象とした転写スクリプト。転写元のレイヤーから転写先のレイヤーへ内容を転写する。レイヤーグループ内での動作や、レイヤーマスクの保持が行われる。',
	# PDBに登録する追加情報
	'かんら・から',					# 作者名
	'GPLv3',					# ライセンス情報
	'2012.12.15',					# 作成日
	'転写(Python)',				# メニューアイテム
	'*',						# 対応する画像タイプ

	[
		(PF_IMAGE, 'image', 'Input image', None),
		(PF_DRAWABLE, 'drawable', 'Input drawable', None)
	],	# プロシジャの引数
	[],	# 戻り値の定義

	python_fu_tensha_2_8,			# 処理を埋け持つ関数名
	menu='<Image>/Layer/レイヤー操作(Python-fu)'	# メニュー表示場所
	)

register(
	'python-fu-clip-layer',			# プロシジャの名前
	'クリップマスク作成スクリプト。下にあるレイヤーから、クリップ用のレイヤーマスクを作成する。',
	# プロシジャの説明文
	'ver 2.8 以上を対象としたクリップマスク作成クリプト。',
	# PDBに登録する追加情報
	'かんら・から',					# 作者名
	'GPLv3',					# ライセンス情報
	'2012.12.15',					# 作成日
	'クリップマスク作成(Python)',			# メニューアイテム
	'*',						# 対応する画像タイプ

	[
		(PF_IMAGE, 'image', 'Input image', None),
		(PF_DRAWABLE, 'drawable', 'Input drawable', None),
		(PF_BOOL, 'searchRecursive',   'レイヤーグループを再帰的に対象とする:', 1),
		(PF_BOOL, 'mergeAlpha', 'アルファチャンネルを参照する:', 1),
		(PF_BOOL, 'mergeLayerMask', 'レイヤーマスクを参照する:', 1),
		(PF_BOOL, 'needCheckVisible', 'レイヤーの表示・非表示を参照する:', 1),
		(PF_BOOL, 'mergeClipLayerMask', 'クリップ作成レイヤーのレイヤーマスクを参照する:', 1),
		(PF_SPINNER, 'searchLayerGroupNumMax', '対象とする同階層下方のレイヤーグループ最大数（無視:0）', 1, (0, 100, 1)),
		# , 0, (0, 100, 1)
		# initial value, (min, max, tick)
		(PF_SPINNER, 'searchLayerNumMax', '対象とするる同階層下方のレイヤー最大数（無視:0）', 0, (0, 100, 1))
	],	# プロシジャの引数
	[],	# 戻り値の定義

	python_fu_clip_layer,			# 処理を埋け持つ関数名
	menu='<Image>/Layer/レイヤー操作(Python-fu)'	# メニュー表示場所
	)


main() # プラグインを駆動させるための関数

